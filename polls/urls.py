from django.urls import path
from polls.views import *

urlpatterns = [
path('', ModelView.as_view(),name='home'),
path('about/',AboutPageView.as_view(),name='about'),
path('blog/<int:pk>/',detail.as_view(),name='detail'),
path('new/',new.as_view(),name='new')
]