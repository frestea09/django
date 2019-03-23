from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'Introduction',
        'isi':'This web is create by Django  and this web tell about music too.',
        'banner':'/img/Introduction.png',
        'nav':[
          ['/home','Home'],
            ['/about','About'],
            ['/music','Music'],
            ['/introduction','Introduction'],
        ],
        'author':'ilman teguh prasetya',

    }
    return render(request,'introduction/main.html',context)