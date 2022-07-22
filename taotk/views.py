from django.shortcuts import render

from dangky.models import Nguoidung

# Create your views here.
def taotk(request):
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    matkhau = request.GET.get('matkhau')
    check = Nguoidung.objects.filter(ten_dang_nhap = ten)
    if check.exists():
        return render(request, 'thatbai.html')
    elif (len(str(ten)) > 10) & (str(mail).count("@")>0):
        data = Nguoidung(
            ten_dang_nhap = ten,
            mail = mail,
            mat_khau = matkhau
        )
        data.save()
        return render(request,'dangnhap.html')
    else: return render(request, 'thatbai.html')