from django.shortcuts import render

def index(request):
    context={
        'judul':'Home',
        'isi':'Welcome to this site this site it\' all about musc',
        'nav':[
            ['/','Home'],
            ['/music','Music'],
            ['/introduction','Introduction'],
            ['/blog','blog'],
        ],
        'author':'ilman teguh prasetya',
    }
    return  render(request,'home_view.html',context)