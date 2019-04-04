from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Introduction',
        'context':'Welcome, this site it\'s make for you who to like music in this world',
        'author':'ilman teguh prasetya',
        'banner':'/img/Introduction.png',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music'],
            ['/about','About'],
            ['/blog','Blog'],
        ],
    }
    return render(request,'introduction/main.html',context)