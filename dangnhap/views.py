from django.shortcuts import render, get_object_or_404
from dangky.models import Nguoidung

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')
def dnthanhcong(request):
    return render(request,'dnthanhcong.html')
def chi_tiet(request, nguoidung_id):
    nguoi_dung = get_object_or_404(Nguoidung, pk = nguoidung_id)
    context = {
        'nguoi_dung':nguoi_dung
    }
    return render(request, "chitiet.html", context)
    
def capnhat(request):
    ten = request.GET.get('ten')
    matkhau = request.GET.get('matkhau')
    mail = request.GET.get('mail')
    id_nguoidung = request.GET.get('id_nd')
    Nguoidung.objects.filter(id =id_nguoidung).update(
        ten_dang_nhap = ten,
        mat_khau = matkhau,
        mail = mail
    )
    danh_sach = Nguoidung.objects.all()
    context = {
        'ds_nguoidung': danh_sach
    }
    return render(request,'danhsach.html', context)

def xoa_nguoidung(request, nguoidung_id):
    dulieu=get_object_or_404(Nguoidung, pk = nguoidung_id)
    try:
        dulieu.delete()
    except:
        print("Xoa bi loi")
    danh_sach = Nguoidung.objects.all()
    context = {
        'ds_nguoidung': danh_sach
    }
    return render(request,'danhsach.html', context)
