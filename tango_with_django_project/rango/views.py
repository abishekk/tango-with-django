# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category

def index(request):
    # obtain the request context
    context = RequestContext(request)

    # obtain the top 5 categories
    category_list = Category.objects.order_by('-likes')[:5]
    # construct template variables as a dictionary
    context_dict = {'categories' : category_list }

    # render it using the django shortcut
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    # obtain the request context
    context = RequestContext(request)

    # construct variables and names as a dictionary
    context_dict = {'profile_image' : 'rango.jpg' }

    # render it using the django shortcut
    return render_to_response('rango/about.html', context_dict, context)
