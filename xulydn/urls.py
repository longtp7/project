from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from xulydn import views

urlpatterns = [
    path('', views.xulydn),
]