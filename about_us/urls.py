from django.urls import path, include
from .views import about_us

urlpatterns = [
    path('', about_us, name='about_us'),
]
