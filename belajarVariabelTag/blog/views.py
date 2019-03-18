from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Blog',
        'isi':'Bagian ini berisi mengenai blog apa saja yang telah ditulis ',
        'author':'ilman teguh prasetya',
        'nav':[
            ['/home','Home'],
            ['/music','Music'],
            ['/introduction','Introduction'],
            ['/blog','blog'],
        ]
    }
    return render(request,'blog/blog_main.html',context)