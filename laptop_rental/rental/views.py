from django.shortcuts import render
from .models import Laptop, Accessory, Insurance

def index(request):
    return render(request, 'rental/index.html')

def laptops(request):
    laptops = Laptop.objects.all()
    return render(request, 'rental/laptops.html', {'laptops': laptops})

def accessories(request):
    accessories = Accessory.objects.all()
    return render(request, 'rental/accessories.html', {'accessories': accessories})

def insurance(request):
    insurance = Insurance.objects.all()
    return render(request, 'rental/insurance.html', {'insurance': insurance})

def rental(request):
    return render(request, 'rental/rental.html')
