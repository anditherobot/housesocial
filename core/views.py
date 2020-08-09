from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template_name = 'core/index.html'
    title = "andi the robot"

    context = {'title': title}
    return render(request, template_name, context)