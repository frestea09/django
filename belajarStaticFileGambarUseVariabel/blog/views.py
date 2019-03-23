from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "judul": "Blog",
        "isi": "This section is tell about other website like Blog and etc",
        "author": "ilman teguh prasetya",
        "banner": "/img/Blog.png",
        "nav": [
            ["/home", "Home"],
            ["/about", "About"],
            ["/music", "Music"],
            ["/blog", "Blog"],
            ["/introduction", "Introduction"],
        ],
    }
    return render(request,'blog/main.html',context)