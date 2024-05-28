from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit', views.edit, name='edit_profile'),
]