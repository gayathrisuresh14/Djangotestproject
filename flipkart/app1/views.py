from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    return HttpResponse("Hi Dears")

def test_func(request):
    return render(request, "test.html")

def samp(request):
    return render(request, "samp.html")

def sample(request):
    return render(request, "samp2.html")