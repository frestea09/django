from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'about/about_main_view.html')
