from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request , "base/home.html" , { "vehicles": vehicles })


def vehicle(request , id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request , "base/vehicle.html" , { "vehicle": vehicle})

def add(request):
    return render(request , "base/add.html")

def update(request , id):
    print(id)
    return render(request , "base/update.html")