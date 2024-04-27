from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=2000, null=True, blank=True)
    numberOfServersHosted = models.IntegerField(default=0)
    currentServer = models.OneToOneField("server_listings_app.Server", on_delete=models.SET_NULL, null=True, blank=True)
    
    def createUserSimple(self,name,password):
        self.username=name
        self.password=password
        self.save()
        return self
    
# Create your models here.
class Server(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    connectionKey = models.CharField(max_length=48, null=True, blank=True)
    dateStarted = models.DateTimeField(auto_now=True, null=True, blank=True)
    dateEnded = models.DateTimeField(auto_now=False, null=True, blank=True)
    
    #plain text password for now we can fix that later
    password = models.CharField(max_length=200, null=True, blank=True)
    
    is_active = models.BooleanField()
    serverClients = models.ManyToManyField(User,  related_name='serverClients', blank=True)
    serverHost = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def createServer(self, title="unspecified",is_active=True):
        self.title=title
        self.is_active=True
        self.save()
        return self
    
