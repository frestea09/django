from django.shortcuts import render
def index(request):
    context={
        'title':'Home',
        'isi':'Selamat Datang diwebsite kami.',
        'nav':[
            ['/home','Home'],
            ['/introduction','Introduction'],
            ['/music','Music']
        ],
        'author':'ilman teguh prasetya',
    }
    return render(request,'main_view.html', context)