from django.shortcuts import render
from core.forms import  RestaurantForm
from core.models import Restaurant, Sales, Rating

# Create your views here.

def index(request):
    # restaurants = Restaurant.objects.all()
    restaurants = Restaurant.objects.prefetch_related('ratings', 'sales')
    context = {
        'restaurants': restaurants
    }
    return render(request, "index.html", context)


def base(request):
    return render(request, 'base.html')