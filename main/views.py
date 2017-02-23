# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})


def item(request, pk):
    return render(request, 'main/item.html', {})


def all_bunche(request):
    return render(request, 'main/all_bunche.html', {})
