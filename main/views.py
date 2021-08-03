from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render


# def index(request):
#     return render(request, 'main/index.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def basket(request):
    return render(request, 'main/basket.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def favorites(request):
    return  render(request, 'main/favorites.html')