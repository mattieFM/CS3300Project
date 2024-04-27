from django import template
from django.urls import reverse
import config
import requests


register = template.Library()


@register.simple_tag(name="serverList", takes_context=True)
def displayServerList(context):
    """A function that will set isDemo to true in the context
        deprecated in v0.1
        use {% ifDemo %} content to display if demo {% endifDemo %} instead
    """
    context['isDemo'] = True


@register.simple_tag(name="joinServer")
def joinServer(serverid, userid):
    requests.post(reverse("server_join",args=[serverid, userid]))
    
@register.simple_tag(name="leaveServer")
def leaveServer(serverid, userid):
    requests.post(reverse("server_leave",args=[serverid, userid]))
