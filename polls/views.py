from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("jango")

def inde(request):
    return HttpResponse('Fa')

def inde1(request):
    return HttpResponse('Fan')

class ModelView(ListView):
    model = blog
    template_name = "home.html"
    context_object_name='post_list'

class AboutPageView(TemplateView): 
    template_name = 'about.html'
    
class detail(DetailView):
    model = blog
    template_name="detail.html"

class new(CreateView):
    model=blog
    template_name='new.html'
    fields = ['title', 'author','body']
    
class edit(UpdateView):
    model=blog
    template_name='edit.html'
    fields=['title','body']
    
class delete(DeleteView):
    model=blog
    template_name='delete.html'
    success_url = reverse_lazy('home')
    
class signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    