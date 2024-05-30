from django.shortcuts import render
from restaurants.models import Restaurant
from articles.models import Article
# Create your views here.
def index(request):
    restaurants = Restaurant.objects.order_by('?')[:4]
    articles = Article.objects.all()

    return render(request, 'main_page/main_page.html', {'restaurants': restaurants, 'articles': articles})