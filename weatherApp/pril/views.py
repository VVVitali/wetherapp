from django.shortcuts import render

def index(request):
    return render(request,('pril/index.html'))

def second(request):
    return render(request,('pril/second.html'))