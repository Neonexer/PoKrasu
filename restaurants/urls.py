from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('/page/', views.restaurants, name='restaurants_'),
    path('/page/<int:page>', views.restaurants, name='restaurants_with_page'),
    path('/<int:restaurant_id>/', views.restaurant_page, name='restaurant_page'),
    path('/<int:restaurant_id>/reviews', views.restaurant_page, name='restaurant_page_'),
    path('/<int:restaurant_id>/reviews/<int:page>', views.restaurant_page, name='restaurant_page_with_review'),
    path('/<int:restaurant_id>/add_to_fav', views.add_to_fav, name='restaurant_page_fav'),
]