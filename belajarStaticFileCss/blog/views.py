from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Blog',
        'content':'Check in our Social Media ',
        'banner':'/img/Blog.png',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music'],
            ['/about','About'],
            ['/blog','Blog'],
        ],
        'author':'ilman teguh prasetya',
    }
    return render(request,'blog/main.html',context)