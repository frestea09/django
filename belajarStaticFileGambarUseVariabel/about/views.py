from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':"about",
        'isi':'this site describe about who we are',
        'author':'ilman teguh prasetya',
        'banner':'/img/About.png',
        'nav':[
            ['/home', 'Home'],
            ['/about', 'About'],
            ['/music', 'Music'],
            ['/introduction', 'Introduction'],
        ],
    }
    return render(request,'about/about_main.html',context)