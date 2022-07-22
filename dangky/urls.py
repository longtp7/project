from django.contrib import admin
from django.urls import path,include
from dangky import views
urlpatterns = [
    path('', views.dangky),
    path('taotk', include('taotk.urls')),
    path('nhapnv', include('nhapnv.urls'))    
]