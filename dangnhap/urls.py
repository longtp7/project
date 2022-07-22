from django.contrib import admin
from django.urls import path,include
from dangnhap import views
urlpatterns = [
    path('', views.dangnhap),
    path('xulydn',include('xulydn.urls')),
    path('nhapnv', include('nhapnv.urls')),
    path('<int:nguoidung_id>/',views.chi_tiet, name="chi_tiet"),
    path('capnhat', views.capnhat, name="xulycapnhat"),
    path('xoa/<int:nguoidung_id>/',views.xoa_nguoidung, name="xoa_nguoidung"),
]