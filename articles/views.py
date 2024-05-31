from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'articles/articles_home.html', {'articles': articles})


def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/article.html', {'article': article})