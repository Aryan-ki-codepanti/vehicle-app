from django.shortcuts import render
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request , "base/home.html" , { "vehicles": vehicles })


def vehicle(request , id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request , "base/vehicle.html" , { "vehicle": vehicle})

def add(request):
    vehicles = Vehicle.objects.all()
    if (request.method == "POST"):
        form = VehicleForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request , "base/home.html",{"obj":obj , "vehicles": vehicles , "alert": "add"})
        
        return render(request , "base/home.html" , { "alert" : "addError" , "vehicles": vehicles })


    form = VehicleForm()
    context = {"form": form}
    return render(request , "base/add.html" , context)

def update(request , id):
    vehicle = Vehicle.objects.get(id=id)
    vehicles = Vehicle.objects.all()

    if (request.method == "POST"):
        form = VehicleForm(data=request.POST,files=request.FILES , instance=vehicle)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request , "base/home.html",{"obj":obj , "vehicles": vehicles , "alert": "update"})
        
        return render(request , "base/home.html" , { "alert" : "updateError" , "vehicles": vehicles , "errors": form.errors })

    
    form = VehicleForm(instance=vehicle)
    context = {"form": form , "vehicle": vehicle}
    return render(request , "base/update.html" , context )