from django.shortcuts import render
import requests


def index(request):
    appid = '92eb8a03f4408b2134d0259be100c9ae'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Гродно'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'speed': res['wind']['speed']
    }

    context = {'info': city_info}
    return render(request, ('pril/index.html'),context)


def second(request):
    appid = '92eb8a03f4408b2134d0259be100c9ae'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Минск'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'speed': res['wind']['speed']
    }

    context = {'info': city_info}
    return render(request, ('pril/second.html'), context)
