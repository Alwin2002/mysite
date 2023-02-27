from django.urls import path
from polls.views import *

urlpatterns = [
path('', ModelView.as_view(),name='home'),
path('about/',AboutPageView.as_view(),name='about'),
path('blog/<int:pk>/',detail.as_view(),name='detail'),
path('new/',new.as_view(),name='new'),
path('edit/<int:pk>/',edit.as_view(),name='edit'),
path('delete/<int:pk>/',delete.as_view(),name='delete'),
path('signup/',signup.as_view(),name='signup')
]