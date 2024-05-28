from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def profile(request):
    return render(request, "profile_page/profile.html")


@login_required
def edit(request):
    return render(request, "profile_page/profile_edit.html")