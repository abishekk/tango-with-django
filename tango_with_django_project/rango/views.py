# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # obtain the request context
    context = RequestContext(request)
    
    # construct template variables as a dictionary
    context_dict = {'boldmessage' : "I am the bold message in the context"}

    # render it using the django shortcut
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return HttpResponse("Rango says: Here is the about page."
                        "<br/> <a href='/rango/'>Home</a>")
