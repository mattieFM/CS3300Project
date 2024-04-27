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
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls as auth_urls
from django.urls import path, include, re_path
from . import views
from .models import Server, User
from .forms import ServerForm, UpdateUserForm, NewUserForm


urlpatterns = [
    #pipe paths directly to our app
    path('', views.search_servers, name="index", kwargs={'activeOnly':True}),
    path('', views.search_servers, name="home", kwargs={'activeOnly':True}),
    path('servers/', views.search_servers, name="search_servers"),
    
    #unknown error
    path('error/', views.error, name="error", kwargs={"err":"unknown error"}),
    
    #login, recovery and register
    path('login/', auth_views.LoginView.as_view(template_name='server_listings_app/pages/auth/login.html'), name="login"),
    path('logout/', views.logout, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='server_listings_app/pages/auth/reset.html'), name="password_reset"),
    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='server_listings_app/pages/auth/reset.html'), name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name='server_listings_app/pages/auth/passwordResetFinished.html'),name="password_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='server_listings_app/pages/auth/reset.html'), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='server_listings_app/pages/auth/reset.html'),name="password_change_done",),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='server_listings_app/pages/auth/resetEmailSent.html'), name="password_reset_done"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/register', views.register, name="register"),
        
    #server details page
    path('server/<int:server_pk>/', views.server, name='server'),
    
    #user details page
    path('user/<int:user_pk>/', views.user, name='user'),
    
    #user & user search
    path('users/', views.user_list, name='users'),
    path('search_users/', views.search_users, name='search_users'),
    
    
    #servers
    re_path(r'^server_update/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':Server, 'Form': ServerForm, 'title':"server"}, name='server_update'),
    re_path(r'^server_create/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':Server, 'Form': ServerForm, 'title':"server"}, name='server_create'),
    re_path(r'^server_delete/(?P<id>[0-9]+)/(?P<backToView>\w*).*', views.generic_delete, {'Model':Server}, name='server_delete'),

    
    #users
    re_path(r'^user_update/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':User, 'Form': UpdateUserForm, 'title':"user", "template_name":"server_listings_app/pages/user/updateProfile.html"}, name='user_update'),
    re_path(r'^user_create/(?P<id>[0-9]+)/(?P<backToView>\w*)/(?P<useArgs>[0,1])/.*', views.generic_update, {'Model':User, 'Form': NewUserForm, 'title':"user", "template_name":"server_listings_app/pages/user/register.html"}, name='user_create'),
    re_path(r'^user_delete/(?P<id>[0-9]+)/(?P<backToView>\w*).*', views.generic_delete, {'Model':User}, name='user_delete'),
    
    #register
    

    #server lobby handlers
    path('server_join/<int:serverid>/<int:clientid>', views.add_client_to_server, name="server_join"),
    path('server_leave/<int:serverid>/<int:clientid>', views.remove_client_from_server, name="server_leave")
]
