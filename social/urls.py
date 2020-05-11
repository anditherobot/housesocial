from django.urls import path

from social.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
