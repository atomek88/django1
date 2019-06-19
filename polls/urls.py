# url.py= URLconf necessary to map view to url
from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),]
