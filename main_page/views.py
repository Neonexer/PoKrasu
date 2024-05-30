from django.shortcuts import render
from restaurants.models import Restaurant
# Create your views here.
def index(request):
    restaurants = Restaurant.objects.order_by('?')[:4]

    return render(request, 'main_page/main_page.html', {'restaurants': restaurants})