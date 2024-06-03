from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles'),
    path('page/', views.index, name='articles_page_1'),
    path('page/<int:page>', views.index, name='articles_page'),
    path('<int:article_id>/', views.article, name='article'),
]