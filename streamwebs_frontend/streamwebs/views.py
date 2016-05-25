from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def index(request):
    return HttpResponse("Hey, you've reached the index.")

def register(request):
    context = RequestContext(request)
    registered = True

    return render_to_response(
        'streamwebs/register.html',
        {'registered': registered}, context)

 
