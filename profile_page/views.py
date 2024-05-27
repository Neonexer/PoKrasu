from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, "profile_page/profile.html")


def edit(request):
    return render(request, "profile_page/profile_edit.html")