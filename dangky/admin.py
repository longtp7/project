from django.contrib import admin
from dangky.models import Nguoidung
# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap','mail')
    list_display_links = ('ten_dang_nhap','mail')
    list_filter = ('ten_dang_nhap','mail')
    search_fields = ('ten_dang_nhap','mail')
    list_per_page = 25
admin.site.register(Nguoidung, NguoiDungAdmin)