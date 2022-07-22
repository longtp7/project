from django.shortcuts import render

# Create your views here.
def dangky(request):
    return render(request,'dangky.html')
def trangchu(request):
    return render(request,'trangchu.html')
def thatbai(request):
    return render(request, 'thatbai.html')