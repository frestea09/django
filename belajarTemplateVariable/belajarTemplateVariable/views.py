from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Welcome This is Home',
        'deskripsi':'ini dibuat menggunakan django 2.1.*'
    }
    return render(request,'main_view.html',context)