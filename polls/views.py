from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("jango")

def inde(request):
    return HttpResponse('Fa')

def inde1(request):
    return HttpResponse('Fan')

class ModelView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView): 
    template_name = 'about.html'