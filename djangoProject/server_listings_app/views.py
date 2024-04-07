import sys
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .models import Server, User


# Create your views here.

#home page
def index(request):
    active_servers = Server.objects.filter(is_active=True)
    # Render index.html
    return render( request, 'server_listings_app/pages/index.html', {'active_servers':active_servers})

def server(request, server_pk):
    # Retrieve the server object using the provided ID
    server = Server.objects.get(pk=server_pk)
    return render( request, 'server_listings_app/pages/serverDetails.html', {'server':server})


def login():
    pass

def logout():
    pass



def generic_update(request, id, Model, Form, returnView, title="server", pk=None):
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
            
            if(pk!=None):
                returnid=str(pk)
            
            return HttpResponseRedirect("/"+returnView+returnid+'/')
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
        
                

            
