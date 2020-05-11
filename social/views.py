from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from .models import TextPost
from .data import feed
from django.core.paginator import Paginator
# Create your views here.

def index (request):
    template_name = 'social/index.html'
    feed_list = feed.get_feed_data()
    paginator = Paginator(feed_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
            'house_users':  User.objects.all(),
            'feed': page_obj
    }
    return render(request, template_name, context)

 
    
        



def profile(request):
    return render(request, 'social/profile.html')
