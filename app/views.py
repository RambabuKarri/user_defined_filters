from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'Hai Ram ,How Are yoU hAHa Hai'}
    return render(request,'usdf.html',d)
