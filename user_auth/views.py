from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = request.POST['username']
            password = request.POST['password1']

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('main_page')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'user_auth/signup.html', context)


def login(request):

    form = LoginForm()
    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('main_page')

    context = {'form': form}

    return render(request, 'user_auth/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('main_page')


# def login(request):
#     error = ''
#     if request.method == "POST":
#         form = LogInForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         if form.is_valid():
#
#             print(request.POST.get('username'))
#             # console.log(request.POST.get('username'))
#             # form.save()
#
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print(username, password)
#             user = auth.authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('main_page')
#         else:
#             error = "Form is not valid"
#             print(form.errors)
#     form = LogInForm()
#
#     data = {"form": form, "error": error}
#
#     return render(request, "user_auth/login.html", data)



# def signup(request):
#     error = ''
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             if request.POST.get('password') == request.POST.get('password2'):
#                 print(request.POST.get('password'))
#                 instance = form.save(commit=False)
#                 instance.password = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()
#
#                 print(instance.password)
#
#                 instance.save()
#                 user = form.instance
#                 auth.login(request, user)
#                 print(request.POST.get('username'))
#                 return redirect('profile')
#             else:
#                 error = "Passwords do not match"
#                 print(error)
#         else:
#             error = "Form is not valid"
#             print(error)
#             print(form.errors)
#
#
#             # Выводить ошибки на экран
#             # Писать куки
#     form = SignUpForm()
#
#     data = {"form": form, "error": error}
#
#     return render(request, "user_auth/signup.html", data)
