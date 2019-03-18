from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul":"Introduction",
        "author":"Deni Jaeni",
        "isi":"Bagian ini merupakan bagian dimana pengenalan web, Website dini dibuat dengan django versi 2.7.*",
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/introduction','Introduction'],
            ['/music','Music'],
        ]
    }
    return render(request,'introduction/introduction_main.html',context)