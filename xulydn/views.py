from django.shortcuts import render

from dangky.models import Nguoidung

# Create your views here.
def xulydn(request):
    ten = request.GET.get('ten')
    matkhau = request.GET.get('matkhau')
    data = Nguoidung.objects.filter(ten_dang_nhap = ten, mat_khau = matkhau)
    if data.exists():
        danh_sach = Nguoidung.objects.all()
        context = {
        'ds_nguoidung': danh_sach
        }
        return render(request,'danhsach.html', context)
    else: return render(request,'dnthatbai.html')