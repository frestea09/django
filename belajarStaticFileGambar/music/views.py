from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "judul":"Music",
        "isi":"Bagian ini berisi mengenai music",
        "author":"Faris Ramdhan",
        "nav":[
            ['/home',"Home"],
            ['/introduction',"Introduction"],
            ['/music',"Music"],
            ['/about',"About"],
        ]
    }
    return render(request,'music/main.html',context)