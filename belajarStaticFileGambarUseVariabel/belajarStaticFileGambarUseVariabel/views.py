from django.shortcuts import render

def index(request):
    context={
        "judul":"Home",
        "isi":"Welcome to this site, this site we made use django 2.* hope you can understand how to use django",
        "author":"ilman teguh prasetya",
        "banner":"/img/Home.png",
        "nav":[
            ["/home","Home"],
            ["/about","About"],
            ["/music","Music"],
            ["/blog","Blog"],
            ["/introduction","Introduction"],
        ],

    }
    return render(request,'main.html',context)