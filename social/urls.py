from django.urls import path

from social.views import *

urlpatterns = [
    path('', index, name='index'),
    path('page<int:page>/', index, name='index'),
]
