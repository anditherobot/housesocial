from django.urls import path
from django.contrib.auth.decorators import login_required
from social.views import *

urlpatterns = [
    path('', index, name='index'),
    path('page<int:page>/', index, name='feed'),
    path('accounts/profile/', login_required(profile_self), name='profile'),
    path('accounts/<str:username>/', profile_others, name='profile_others'),
    path('message/<str:did>/', messages, name='messages'),

]
