from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "blog/home.html")
def About(request):
    return HttpResponse("<B><h1>Blog About</h1></B>")

