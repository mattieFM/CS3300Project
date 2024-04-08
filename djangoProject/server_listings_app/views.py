import sys
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .models import Server, User


# Create your views here.

#home page
def index(request):
    active_servers = Server.objects.filter(is_active=True)
    # Render index.html
    return render( request, 'server_listings_app/pages/index.html', {'active_servers':active_servers})

def search_servers(request, activeOnly=False):
    query = request.GET.get('q')
    if(query == None):
        query=""
    #name__icontains is case insenstitive containment test see: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#icontains
    servers = Server.objects.filter(title__icontains=query)
    if(activeOnly):
        servers = servers.filter(is_active=True)
    # Render index.html
    return render( request, 'server_listings_app/pages/servers.html', {'active_servers':servers})

def server(request, server_pk):
    # Retrieve the server object using the provided ID
    server = Server.objects.get(pk=server_pk)
    return render( request, 'server_listings_app/pages/serverDetails.html', {'server':server})

def user(request, user_pk):
    # Retrieve the server object using the provided ID
    user = User.objects.get(pk=user_pk)
    return render( request, 'server_listings_app/pages/userDetails.html', {'user':user})

#student list page
def user_list(request):
    users = User.objects.all()
    return render(request, 'server_listings_app/pages/user_list.html', {'users': users})

#querried student list page
def search_users(request):
    query = request.GET.get('q')
    #name__icontains is case insenstitive containment test see: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#icontains
    users = User.objects.filter(username__icontains=query)
    return render(request, 'server_listings_app/pages/user_list.html', {'users': users})

def login():
    pass

def logout():
    pass

def generic_update(request, id, Model, Form, title, backToView, useArgs):
    """
    useArgs: whether to use args or returnid"""
    path=request.path
    pathArgs=path.split('/')[6:]
    id=int(id)
    form = None
    model = None
    if(id==0):
        form = Form()
    else:
        model = Model.objects.get(pk=id)
        form = Form(instance=model)
       
    # Retrieve the portfolio object using the provided ID
    
    # create a form instance and populate it with data from the request:
    if request.method == "POST":
        form = Form(request.POST, instance=model)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            model = form.save()          
            returnid=str(model.pk)
            if(not returnid):
                returnid=id
            
            args=[returnid]
            if(useArgs=='1'):
                args=pathArgs
                            
            return HttpResponseRedirect(reverse(backToView, args=args))
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'server_listings_app/pages/genericFormUpdate.html', {"form": form, "title": title, "model":model})

def generic_delete(request, id, Model, backToView=None):
    """request: django request
        id: django pk 
        model: the model that the pk is for
        backtoView the name of the view to reutrn to
        backToPk is the id"""
    # Retrieve the portfolio object using the provided ID
    path=request.path
    pathArgs=path.split('/')[4:]
    id=int(id)
    print(id, file=sys.stderr)
    print(backToView, file=sys.stderr)
    model = None
    try:
        model = Model.objects.get(pk=id)
    except:
        pass
    
    if request.method == "POST":
        if(model != None):
            model.delete()
        
        redirect=False
        if(backToView != None):
            if(len(backToView)>0 and backToView != 'none'):
                redirect=True
                
        #if path provided a valid redirect immediately go to that page
        if(redirect):
            return HttpResponseRedirect(reverse(backToView, args=pathArgs))
        else:
            return render(request, 'server_listings_app/pages/deleted.html')
        
                

def add_client_to_server(reqeust, clientid, serverid):
    try:
        server = Server.objects.get(pk=serverid)
        user=User.objects.get(pk=clientid)
        user.currentServer=server
        server.serverClients.add(user)
        return JsonResponse({'status':200})
    except Exception as err:
        return JsonResponse({'status':400,'err':err})

    
def remove_client_from_server(reqeust, clientid, serverid):
    try:
        server = Server.objects.get(pk=serverid)
        user=User.objects.get(pk=clientid)
        user.currentServer=None
        server.serverClients.remove(user)
        return JsonResponse({'status':200})
    except Exception as err:
        return JsonResponse({'status':400,'err':err})