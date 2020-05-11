from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'social/index.html')

def profile(request):
    return render(request, 'social/profile.html')