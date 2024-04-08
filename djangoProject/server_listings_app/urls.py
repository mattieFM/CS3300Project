"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .models import Server, User
from .forms import ServerForm, UserForm

urlpatterns = [
    #pipe paths directly to our app
    path('', views.search_servers, name="index", kwargs={'activeOnly':True}),
    path('servers/', views.search_servers, name="search_servers"),
    
    #temp login functionality
    path('', views.search_servers, name="login"),
    path('', views.search_servers, name="logout"),
        
    #server details page
    path('server/<int:server_pk>/', views.server, name='server'),
    
    #user details page
    path('user/<int:user_pk>/', views.user, name='user'),
    
    #user & user search
    path('users/', views.user_list, name='users'),
    path('search_users/', views.search_users, name='search_users'),
    
    
    #server update page
    re_path(r'^server_update/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':Server, 'Form': ServerForm, 'title':"server"}, name='server_update'),
    re_path(r'^server_create/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':Server, 'Form': ServerForm, 'title':"server"}, name='server_create'),
    re_path(r'^server_delete/(?P<id>[0-9]+)/(?P<backToView>\w*).*', views.generic_delete, {'Model':Server}, name='server_delete'),

    
    #user update page
    re_path(r'^user_update/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':User, 'Form': UserForm, 'title':"user"}, name='user_update'),
    re_path(r'^user_create/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':User, 'Form': UserForm, 'title':"user"}, name='user_create'),
    re_path(r'^user_delete/(?P<id>[0-9]+)/(?P<backToView>\w*).*', views.generic_delete, {'Model':User}, name='user_delete'),

    #server lobby handlers
    path('server_join/<int:serverid>/<int:clientid>', views.add_client_to_server, name="server_join"),
    path('server_leave/<int:serverid>/<int:clientid>', views.remove_client_from_server, name="server_leave")
]
