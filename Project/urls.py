from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls'), name='main'),
    path('restaurants', include('restaurants.urls'), name='restaurants'),
    path('articles/', include('articles.urls'), name='articles'),
    path('accounts/', include('user_auth.urls'), name='accounts'),
    path('profile/', include('profile_page.urls'), name='profile'),
    # path('restaurants/', include('restaurants.urls'), name='restaurants'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
