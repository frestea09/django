from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'Introduction',
        'isi':'Bagian ini menjelaskan mengenai pengenalanwebsite ini',
        'author':'ilman teguh prasetya',
        'nav':[
            ['/home','Home'],
            ['/music','Music'],
            ['/introduction','Incroduction'],
            ['/about','About'],
        ],
    }
    return render(request,'intorduction/main.html',context)