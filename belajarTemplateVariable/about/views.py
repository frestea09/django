from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'Author'
    }
    return render(request,'about/about_main_view.html',context)
def autorSatu(request):
    context={
        'judul':'Author',
        'nama':'ilman teguh prasetya',
        'author':'Cerita',
    }
    return render(request,'about/about_main_view.html',context)
def authorDua(request):
    context={
        'judul':'Author',
        'nama':'Lies Hartiani',
        'author':'Resep',
    }
    return render(request,'about/about_main_view.html',context)