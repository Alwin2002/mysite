from django.urls import path
from polls.views import *

urlpatterns = [
path('', ModelView.as_view(),name='home'),
path('about/',AboutPageView.as_view(),name='about')
]