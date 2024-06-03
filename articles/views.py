from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request, page=1):
    paginator = Paginator(Article.objects.all(), 5)
    page = paginator.page(page)
    articles = Article.objects.order_by('-date')
    return render(request, 'articles/articles_home.html', {
        'paginator': paginator,
        'page': page,
    })


def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/article.html', {'article': article})