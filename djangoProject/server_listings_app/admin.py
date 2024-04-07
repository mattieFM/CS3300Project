from django.contrib import admin

from django.apps import apps

models = apps.get_models()

#you need to verify models are not already registered otherwise the admin login will break
for model in models:
    if(model):
        if(not admin.site.is_registered(model)):
            admin.site.register(model)