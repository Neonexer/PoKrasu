from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profile_page.models import Favorite
from restaurants.models import Restaurant, Review
from user_auth.forms import EditProfileForm
from user_auth.models import User


# Create your views here.

@login_required
def profile(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)

    restaurants = Restaurant.objects.all()

    restaurant_reviews = {}
    for i in restaurants:
        review_count = Review.objects.filter(restaurant=i).count()
        restaurant_reviews[i] = review_count

    return render(request, "profile_page/profile.html", {
        "favorites": favorites,
        "restaurant_reviews": restaurant_reviews,
    })


@login_required
def edit(request):
    current_user = User.objects.get(id=request.user.id)
    form = EditProfileForm(request.POST or request.FILES or None, instance=current_user)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=current_user)
    if form.is_valid():
        form.save()
        messages.success(request, "Your profile has been updated!")
        print(1)
        return redirect("profile")
    else:
        print(form.errors)
        print(2)
        return render(request, "profile_page/profile_edit.html", {"form": form})