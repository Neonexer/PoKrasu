from django.shortcuts import render
from restaurants.models import Restaurant, Review
from articles.models import Article
# Create your views here.
def index(request):
    restaurants = Restaurant.objects.order_by('?')[:4]
    articles = Article.objects.all()[:6]

    restaurant_reviews = {}
    for i in restaurants:
        review_count = Review.objects.filter(restaurant=i).count()
        restaurant_reviews[i] = review_count

    return render(request, 'main_page/main_page.html', {
        'restaurants': restaurants,
        'articles': articles,
        'restaurant_reviews': restaurant_reviews
    })