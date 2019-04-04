from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'Introduction',
        'isi': 'Welcome this section it\s introduction what we make this web we create user django 2.* ',
        'banner': 'img/Introduction.png',
        'nav': [
            ['/home', 'Home'],
            ['/introduction', 'Introduction'],
        ],
        'author': 'ilman teguh prasetya',
    }
    return render(request,'introduction/main.html',context)