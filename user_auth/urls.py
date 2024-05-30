from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    # path('', views.login, name='login'),
    # path("signup", views.signup, name='signup'),
]