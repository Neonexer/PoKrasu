from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm
# Create your views here.
def login(request):
    error = ''
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = "Form is not valid"
    form = LogInForm()

    data = {"form": form, "error": error}

    return render(request, "user_auth/login.html", data)


def signup(request):
    error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        else:
            error = "Form is not valid"
    form = SignUpForm()

    data = {"form": form, "error": error}

    return render(request, "user_auth/signup.html", data)