from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from .models import TextPost
from .data import feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index (request):
    template_name = 'social/index.html'
    feed_list = feed.get_feed_data()
    page = request.GET.get('page', 1)
    paginator = Paginator(feed_list, 3)
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
            'house_users':  User.objects.all(),
            'feed': page_obj
    }
    return render(request, template_name, context)

 
    
        



def profile_self(request):
    return render(request, 'social/profile.html')

def profile_others(request, username):
    template_name = ('social/profile-others.html')
    user = User.objects.get(username= username)
    context = {"user": user}
    return render(request, template_name, context)
