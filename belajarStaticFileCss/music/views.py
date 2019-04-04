from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Music',
        'context':'Introduction  the sound who will make  the great think in the world , this site make you\'r mod again.',
        'banner':'img/Music.png',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music'],
            ['/about','About'],
            ['/blog','Blog'],
        ],
        'author':'ilman teguh prasetya'
    }
    return render(request,'music/main.html',context)