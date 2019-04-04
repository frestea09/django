from django.shortcuts import render

def index(request):
    context = {
        'title':'Home',
        'isi':'This,Page is main page in this website. and we call it\t Home',
        'nav':[
            ['\home','Home'],
            ['\introduction','Intorduction'],
        ],
        'author':'ilman teguh prasetya',
        'banner':'/img/Home.png',
    }
    return render(request,'home.html',context)