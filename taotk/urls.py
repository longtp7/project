from django.contrib import admin
from django.urls import path
from taotk import views

urlpatterns = [
    path('', views.taotk),
]