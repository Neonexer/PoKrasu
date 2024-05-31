from django.contrib import admin

from restaurants.models import Address, Restaurant, Review

# Register your models here.
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Review)
