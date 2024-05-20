from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-date')
    return render(request, 'articles/articles_home.html', {'articles': articles})