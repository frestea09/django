from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'Welcome to Blog',
        'deskripsi': 'Website ini dibuat meggunakan Django 2.1.*',
    }
    return render(request,'blog/main_view.html',context)
def cerita(request):
    context={
        'judul':'Welcome to Cerita',
        'deskripsi':'Bagian ini menceritakan tentang cerita',
        'pengarang':'ilman teguh prasetya',
    }
    return render(request,'blog/main_view.html',context)
def resep(request):
    context={
        'judul':'Welcome to Resep',
        'deskripsi':'Bagian ini menceritakan mengenai Resep',
        'pengarang':'lies hartiani',
    }
    return render(request,'blog/main_view.html',context)