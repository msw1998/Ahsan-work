from django.shortcuts import render
from django.utils.timezone import now

from .models import Product


# Create your views here.
def home(request):
    return render(request, 'myapp/index.html', {'timestamp': now().timestamp()})

def explore(request):
    return render(request, 'myApp/explore.html')  # Explore Page

def fitness(request):
    return render(request, 'myApp/fitness.html')  # Fitness Page

def nutrition(request):
    return render(request, 'myApp/nutrition.html')# Nutrition Page

def settings(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'myApp/settings.html', {'products': products}) # Settings Page