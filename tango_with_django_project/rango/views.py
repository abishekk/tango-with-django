# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category
from rango.models import Page

def index(request):
    # obtain the request context
    context = RequestContext(request)

    # obtain the top 5 categories
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    # construct template variables as a dictionary

    for category in category_list:
        category.url = category.name.replace(' ', '_')

    context_dict = {'categories' : category_list, 'pages' : page_list }

    # render it using the django shortcut
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    # obtain the request context
    context = RequestContext(request)

    # construct variables and names as a dictionary
    context_dict = {'profile_image' : 'rango.jpg' }

    # render it using the django shortcut
    return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
    # Request context from the request passed to us
    context = RequestContext(request)

    # Change underscores in the category name to spaces
    category_name = category_name_url.replace('_', ' ')

    context_dict = {'category_name' : category_name}

    try:
        category = Category.objects.get(name = category_name)

        pages = Page.objects.filter(category = category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)
