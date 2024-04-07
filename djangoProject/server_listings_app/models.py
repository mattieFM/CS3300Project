from django.db import models

# Create your models here.
class Server(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    connectionKey = models.CharField(max_length=48, null=True, blank=True)
    
    #plain text password for now we can fix that later
    password = models.CharField(max_length=200, null=True, blank=True)
    
    is_active = models.BooleanField()
    serverClients = models.ManyToManyField('server_listings_app.User',  related_name='serverClients', null=True, blank=True)
    serverHost = models.OneToOneField("server_listings_app.User", on_delete=models.SET_NULL, null=True, blank=True)
    
class User(models.Model):
    username = models.CharField(max_length=200)