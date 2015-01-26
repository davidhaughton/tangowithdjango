from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!"+
                        "\n <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page." +
                        "\n This tutorial has been put together by David Haughton, 2080734h"+
                        "\n <a href='/rango/'>Index</a>")
