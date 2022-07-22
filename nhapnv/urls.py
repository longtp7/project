from django.contrib import admin
from django.urls import path,include
from nhapnv import views

urlpatterns = [
    path('', views.nhapnv),
    # path('', views.xemds)
]