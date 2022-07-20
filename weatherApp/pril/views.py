from django.shortcuts import render
import requests


def index(request):
    appid = '92eb8a03f4408b2134d0259be100c9ae'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Grodno'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, ('pril/index.html'))


def second(request):
    return render(request, ('pril/second.html'))
