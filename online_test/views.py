from django.shortcuts import redirect,render

from .settings import URL_ROOT


def index(request):
    return render(request,'landing.html')
