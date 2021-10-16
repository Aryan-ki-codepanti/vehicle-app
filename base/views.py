from django.shortcuts import redirect, render
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
        
            return redirect("/")


    form = VehicleForm()
    context = {"form": form}
    return render(request , "base/add.html" , context)

def update(request , id):
    vehicle = Vehicle.objects.get(id=id)
    vehicles = Vehicle.objects.all()

    if request.method == "POST":
        form = VehicleForm(data=request.POST,files=request.FILES , instance=vehicle)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect("/")
        
    
    form = VehicleForm(instance=vehicle)
    context = {"form": form , "vehicle": vehicle}
    return render(request , "base/update.html" , context )

def delete(request , id):
    vehicle = Vehicle.objects.get(id=id)
    vehicles = Vehicle.objects.all()

    if request.method == "POST":
        vehicle.delete()
        return redirect("/")

    
        
    # get request
    return render(request , "base/delete.html" , {"vehicle": vehicle })

def about(request):
    return render(request , "base/about.html")