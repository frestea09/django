from django.shortcuts import render

def index(request):
    context={
        'title':'Home',
        'content':'Welcome to this website Let\'s play',
        'banner':'/img/Home.png',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music'],
            ['/about','About'],
            ['/blog','Blog'],
        ],
        'author':'ilman teguh prasetya',
    }
    return render(request,('main.html'),context)