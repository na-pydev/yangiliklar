from django.core import paginator
from django.http import request
from django.shortcuts import render
from .models import Xabar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests

def bosh_sahifa(request):

    xabarlar = Xabar.elon_qilingan.all()

    soz = request.GET.get('soz')
    natija = []
    if soz != None:
        for xabar in xabarlar:
            if soz.lower() in xabar.mavzu.lower() or soz.lower() in xabar.matn.lower():
                natija.append(xabar)
        xabarlar = natija
    

    paginator = Paginator(xabarlar, 4)
    page = request.GET.get('page')

    try:
        xabarlar = paginator.page(page)
    except PageNotAnInteger:
        xabarlar = paginator.page(1)
    except EmptyPage:
        xabarlar = paginator.page(paginator.num_pages)

    n = len(xabarlar)


    context={'xabarlar': xabarlar, 'page': page, 'soz':soz, 'n': n}



    return render(request, 'xabar/bosh_sahifa.html', context )


def info(request, xabar_id):

    xabar = Xabar.objects.get(id=xabar_id)

    xabar.korildi = xabar.korildi + 1
    xabar.save()

    context = {'xabar': xabar,}

    return render(request, 'xabar/info.html', context)


def toifa(request, toifa):
    xabarlar = Xabar.elon_qilingan.filter(toifa=toifa)

    soz = request.GET.get('soz')
    natija = []
    if soz != None:
        for xabar in xabarlar:
            if soz.lower() in xabar.mavzu.lower():
                natija.append(xabar)
        xabarlar = natija
    

    paginator = Paginator(xabarlar, 4)
    page = request.GET.get('page')

    try:
        xabarlar = paginator.page(page)
    except PageNotAnInteger:
        xabarlar = paginator.page(1)
    except EmptyPage:
        xabarlar = paginator.page(paginator.num_pages)

    n = len(xabarlar)

    context={'xabarlar': xabarlar, 'page': page, 'n':n}



    return render(request, 'xabar/bosh_sahifa.html', context )


def ob_havo(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6399e18ac9a5e1eefa3cc42d56c07e24&lang={}'
    shahar = 'Tashkent'
    til = 'uz'
    shahar_havosi = requests.get(url.format(shahar, til)).json()

    harorat = (int(shahar_havosi['main']['temp']) - 32)*5/9
    tarif = shahar_havosi['weather'][0]['description']
    v = {"mist": 'tuman'}
    havo = {
        'shahar' : shahar,
        'harorat' : harorat,
        'tarif' : v.get(tarif, None),
        'belgi' : shahar_havosi['weather'][0]['icon']
    }

    return render(request, 'xabar/ob-havo.html',{'ob_havo': havo})


