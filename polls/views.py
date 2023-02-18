from django.http import HttpResponse
from django.views.generic import ListView,TemplateView
from .models import Post

def index(request):
    return HttpResponse("jango")

def inde(request):
    return HttpResponse('Fa')

def inde1(request):
    return HttpResponse('Fan')

class ModelView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name='post_list'

class AboutPageView(TemplateView): 
    template_name = 'about.html'