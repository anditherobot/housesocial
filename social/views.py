from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import TextPost
from .data import feed
# Create your views here.

class IndexView (TemplateView):
    template_name =  'social/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['house_users'] = User.objects.all()
        context['feed'] = feed.get_feed_data()
        
        return context

def profile(request):
    return render(request, 'social/profile.html')
