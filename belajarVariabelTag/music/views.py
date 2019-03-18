from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'Music',
        'author':'fairs syahroni ramdhan',
        'isi':'Bagian ini berisi tentang berbagai macam music yang ada pada zaman sekarang',
        'nav':[
            ['/home','Home'],
            ['/about','About'],
            ['/music','Music'],
            ['/introduction','Introduction'],
        ]

    }
    return render(request,'music/music_main.html',context)