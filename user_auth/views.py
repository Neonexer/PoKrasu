import hashlib
from django.core.mail.backends import console
from django.shortcuts import render, redirect

from user_auth.forms import LogInForm, SignUpForm


# Create your views here.

def login(request):
    error = ''
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():

            print(request.POST.get('username'))
            # console.log(request.POST.get('username'))
            form.save()
            return redirect('articles')
        else:
            error = "Form is not valid"
            print(form.errors)
    form = LogInForm()

    data = {"form": form, "error": error}

    return render(request, "user_auth/login.html", data)


def signup(request):
    error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            if request.POST.get('password') == request.POST.get('password2'):
                print(request.POST.get('password'))
                instance = form.save(commit=False)
                instance.password = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()

                print(instance.password)

                instance.save()
                print(request.POST.get('username'))
                return redirect('profile')
            else:
                error = "Passwords do not match"
                print(error)
        else:
            error = "Form is not valid"
            print(error)
            print(form.errors)


            # Выводить ошибки на экран
            # Писать куки
    form = SignUpForm()

    data = {"form": form, "error": error}

    return render(request, "user_auth/signup.html", data)
