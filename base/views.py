from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle

# Create your views here.

def home(request):
    return HttpResponse("Home here")


def vehicle(request , id):
    vehicle = Vehicle.objects.get(id=id)
    print(vehicle)
    return HttpResponse("Vehicle Here")

def add(request):
    return HttpResponse("add vehicle here")

def update(request , id):
    print(id)
    return HttpResponse("update vehicle here")