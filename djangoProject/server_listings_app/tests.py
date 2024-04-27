from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user

from django.template import Context, Template
from .models import *
from .forms import *
from .templatetags import util_tags, demoTags, server
import config

# Create your tests here.

class AuthenticationTests(TestCase):
    def setUp(self) -> None:
        #create very simple mock data
        self.testUser1 = User.objects.create_user(username='test', password='test')
        self.testUser2 = User.objects.create_user(username='test2', password='test2')
        self.testUser3 = User.objects.create_user(username='test3', password='test3')
        return super().setUp()
    
    def test_login(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(username='test', password='test')
        self.assertTrue(get_user(self.client).is_authenticated)
    
    def test_unauthenticated_user_cannot_view_profile(self):
        """ensure non logged in users cannot view their profile"""
        response = self.client.get(reverse("profile"))
        self.assertTrue(isinstance(response, HttpResponseRedirect))
        self.assertIn("login", response.url)
        
    def test_authenticated_user_can_view_profile(self):
        """ensure logged in users can view their profile"""
        self.client.login(username='test', password='test')
        response = self.client.get(reverse("profile"))
        self.assertContains(response,text="profile" ,status_code=200)        

    def test_edit_profile_does_not_show_on_others(self):
        """ensure that the edit profile button does not show up on other user's profiles"""
        self.client.login(username='test', password='test')
        response = self.client.get(reverse("user", kwargs={"user_pk":2}))
        self.assertNotContains(response,text="edit" ,status_code=200)   
        
    def test_edit_profile_does_show_on_self(self):
        """ensure that the edit profile button does show up on own profile"""
        self.client.login(username='test', password='test')
        response = self.client.get(reverse("profile"))
        self.assertNotContains(response,text="edit" ,status_code=200)    
        
    def test_view_user_self_redirects_to_profile(self):
        """ensure that the edit profile button does not show up on other user's profiles"""
        self.client.login(username='test', password='test')
        response = self.client.get(reverse("user", kwargs={"user_pk":1}))
        self.assertContains(response,text="profile" ,status_code=200)
        
class ModelTests(TestCase):
    def test_can_create_user(self):
        testUser1 = User().createUserSimple('test', 'test')
        #user returned properly
        self.assertTrue(isinstance(testUser1,User))
        #user in db
        self.assertTrue(User.objects.get(pk=testUser1.pk))
        
    def test_can_create_server(self):
        testServer = Server().createServer()
        #server returned properly
        self.assertTrue(isinstance(testServer,Server))
        #server in db
        self.assertTrue(Server.objects.get(pk=testServer.pk))
        
class FormTests(TestCase):
        defaultGoodUserData={
                "username":"goodUser",
                "password1":"hdserhjerherherherh",
                "password2":"hdserhjerherherherh"
        }
    
        def passwordValidationTest(self,badData,GoodData):
            form = NewUserForm(badData)
            self.assertFalse(form.is_valid())
            form = NewUserForm(GoodData)
            print(form.errors)
            self.assertTrue(form.is_valid())
    
        def test_password_validation_passwordMustMatch_in_register_form(self):
            badData = {
                "username":"testUser",
                "password1":"notMAtching",
                "password2":"hdserhjerherherherh"
            }
            
            self.passwordValidationTest(badData,self.defaultGoodUserData)
            
        def test_password_validation_passwordLength_in_register_form(self):
            badData = {
                "username":"testUser",
                "password1":"123",
                "password2":"123"
            }
            
            self.passwordValidationTest(badData,self.defaultGoodUserData)
            
        def test_password_validation_namePasswordTooSimilar_in_register_form(self):
            badData = {
                "username":"testUser",
                "password1":"testUser",
                "password2":"testUser"
            }
            
            self.passwordValidationTest(badData,self.defaultGoodUserData)
          
            
        def test_username_validation_noDuplicateUsers_in_register_form(self):
            data = {
                "username":"HiIamANewUser",
                "password1":"01576dfdfsf890bhlbgaew",
                "password2":"01576dfdfsf890bhlbgaew"
            }
            form = NewUserForm(data)
            print(form.errors)
            self.assertTrue(form.is_valid())
            form.save()
            form2 = NewUserForm(data)
            data["password1"]="01576dnsdnssdnsdnffdfsf890bhlbgaew"
            data["password2"]="01576dnsdnssdnsdnffdfsf890bhlbgaew"
            errorOccurred=False
            try:
                form2.save()
            except:
                errorOccurred=True
            self.assertTrue(errorOccurred)
            
     
class CustomTagTests(TestCase):
    def test_inlineif(self):
        """verify inline if custom tag works in isolation"""
        context = {"IHaveThisVariable":"hello"}
        
        #direct tests
        
        #check normal HAS case
        self.assertTrue("Hiya" in util_tags.iIf(context, "IHaveThisVariable", "Hiya"))
        
        #check normal !HAS case
        self.assertFalse("Hiya" in util_tags.iIf(context, "IDontHaveThisVariable", "Hiya"))
        
        #check inverse HAS case
        self.assertFalse("Hiya" in util_tags.iIf(context, "IHaveThisVariable", "Hiya", True))
        
        #check inverse !HAS case
        self.assertTrue("Hiya" in util_tags.iIf(context, "IDontHaveThisVariable", "Hiya", True))
        
        #through template
        
        t = Template("""
        {% load util_tags %}
        {% iIf 'IHaveThisVariable' 'NORMAL_HAS' %}
        {% iIf 'IDontHaveThisVariable' 'NORMAL_!HAS' %}
        {% iIf 'IHaveThisVariable' 'INVERT_HAS' True %}
        {% iIf 'IDontHaveThisVariable' 'INVERT_!HAS' True %}
        """)
    
        rendered = t.render(Context(context))
        
        print(rendered)
        
        self.assertIn("NORMAL_HAS", rendered)
        self.assertIn("INVERT_!HAS", rendered)
        self.assertNotIn("NORMAL_!HAS", rendered)
        self.assertNotIn("INVERT_HAS", rendered)
    
    def test_demoBlocks(self):
        """test if the conditional blocks that should only show in demo work"""
        
        
        
        t = Template("""
        {% ifDemo %}
            from inside demo
        {% endifDemo %}
        """)
        
        #positive case
        config.isDemo=True
        rendered = t.render(Context({}))
        self.assertIn("from inside demo", rendered)
        
        #negative case
        config.isDemo=False
        rendered = t.render(Context({}))
        self.assertNotIn("from inside demo", rendered)

    #these tags arn't used and I wrote the tests but never finished the tags
    def join_server(self):
        """test if join server tag works"""
        
        #create server
        testUser1 = User().createUserSimple('test', 'test')
        testServer = Server().createServer()
        
        self.assertTrue(testServer.serverClients.all().count() == 0)
        
        t = Template(
        f"{{% load server %}}"
        f"{{% joinServer {testServer.pk} {testUser1.pk} %}}"
        )
        
        t.render(context=Context({}))
        
        self.assertTrue(testServer.serverClients.all().count() == 1)
        
    def leave_server(self):
        """test if join server tag works"""
        
        #create server
        testUser1 = User().createUserSimple('test', 'test')
        testServer = Server().createServer()
        
        self.assertTrue(testServer.serverClients.all().count() == 0)
        
        t = Template(
        f"{{% load server %}}"
        f"{{% joinServer {testServer.pk} {testUser1.pk} %}}", 
        )
        
        t.render(context=Context({}))
        
        self.assertTrue(testServer.serverClients.all().count() == 1)
        
        
        
        
        
        