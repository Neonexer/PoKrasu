from sqlite3 import IntegrityError

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import json

from profile_page.models import Favorite
from user_auth.models import User
from .forms import ReviewForm
from .models import Restaurant, Review

from django.db import IntegrityError


# Create your views here.
def restaurants(request, page=1):

    # file = "/Users/max/PycharmProjects/Project/restaurants/static/restaurants/result.json"
    #
    # data2 = []
    #
    # with open(file, mode='r') as file:
    #     data = json.load(file)
    #
    # for el in data:
    #     # print(el)
    #
    #     try:
    #         address = el.get("address")
    #     except Exception as e:
    #         print(e)
    #         street = ""
    #         home = ""
    #         continue
    #
    #     name = el.get("name")
    #     type = el.get("type")
    #
    #     try:
    #         rating = el.get("raiting").replace(",", ".")
    #         rating = str(rating)
    #     except Exception as e:
    #         print(e)
    #         continue
    #     try:
    #         image = el.get("img")[1]
    #     except:
    #         continue
    #     # print(name)
    #     # print(type)
    #     # print(rating)
    #     # # print(address)
    #     # print(street)
    #     # print(home)
    #     # print(image)
    #     data2.append({
    #         "name": name,
    #         "address": address,
    #         "type": type,
    #         "image": image,
    #         "rating": rating
    #     })
    #
    #     # print(street, home)
    #     address = Address(address=address)
    #     restaurant = Restaurant(name=name, type=type, address=address, rating=rating, image=image)
    #     address.save()
    #     restaurant.save()
    #
    # print(len(data))


    # return render(request,"restaurants/rest.html", context={"data":data2})

    paginator = Paginator(Restaurant.objects.all(), 10)
    # print(paginator.count)
    # print(paginator.num_pages)
    # print(page)

    restaurants = Restaurant.objects.all()

    restaurant_reviews = {}
    for i in restaurants:
        review_count = Review.objects.filter(restaurant=i).count()
        restaurant_reviews[i] = review_count


    return render(request,"restaurants/restaurants.html", {
        "restaurants":restaurants,
        "count":restaurants.count(),
        "restaurant_reviews":restaurant_reviews,
        "paginator":paginator,
        "page":paginator.page(page),
    })


def restaurant_page(request, restaurant_id, page=1):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    reviews = Review.objects.filter(restaurant_id=restaurant_id)
    reviews_count = reviews.count()

    paginator = Paginator(reviews, 3)

    form = ReviewForm()
    if request.method == "POST" and User.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        review = Review(restaurant=restaurant, user=user, text=request.POST["text"])
        review.save()
        return redirect('restaurant_page', restaurant_id)

    print(restaurant.name)
    return render(request, "restaurants/restaurant_page.html", {
        "restaurant":restaurant,
        "form":form,
        "reviews":reviews,
        "reviews_count":reviews_count,
        "paginator":paginator,
        "page":paginator.page(page),
    })

@login_required
def add_to_fav(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    user = User.objects.get(pk=request.user.id)
    try:
        favorite = Favorite(restaurant=restaurant, user=user)
        favorite.save()
    except IntegrityError:
        # favorite = Favorite(restaurant=restaurant, user=user)
        # favorite.delete()
        Favorite.objects.filter(restaurant=restaurant, user=user).delete()
        # print("Favorite already exists")
    return redirect('restaurant_page', restaurant_id)