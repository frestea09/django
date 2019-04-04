from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'About',
        'content':'this will tell about us who it make it and work on this project',
        'author':'ilman teguh prasetya',
        'banner':'/img/About.png',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music'],
            ['/about','About'],
            ['/blog','Blog'],
        ]
    }
    return render(request,'about/main.html',context)