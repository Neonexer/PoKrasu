from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants'),
    path('/<int:restaurant_id>/', views.restaurant_page, name='restaurant_page'),
    path('/<int:restaurant_id>/add_to_fav', views.add_to_fav, name='restaurant_page_fav'),
]