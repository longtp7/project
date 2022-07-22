from django.shortcuts import render
from nhapnv.models import NhanVien
# Create your views here.
def nhapnv(request):
    hoten = request.GET.get('hoten')
    chucvu = request.GET.get('chucvu')
    namsinh = request.GET.get('namsinh')
    if (len(str(hoten))>1) & (len(str(chucvu))>1):
        data = NhanVien(
                ho_ten = hoten,
                chuc_vu = chucvu,
                namsinh = namsinh
            )
        data.save()
        return render(request,'dnthanhcong.html')
    else: return render(request,'nhapthatbai.html')
# def xemds(request):
#     ten = request.GET.get('ten')
#     matkhau = request.GET.get('matkhau')
#     data = Nguoidung.objects.filter(ten_dang_nhap = ten, mat_khau = matkhau)
#     if data.exists():
#         danh_sach = Nguoidung.objects.all()
#         context = {
#         'ds_nguoidung': danh_sach
#         }
#         return render(request,'danhsach.html', context)
#     else: return render(request,'dnthatbai.html')