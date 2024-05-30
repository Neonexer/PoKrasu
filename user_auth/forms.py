from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from .models import User
from django.forms import ModelForm, TextInput, EmailInput
# from django.contrib.auth.models import User
from .models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput


# Create a User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# Authenticate a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))

# class SignUpForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#         widgets = {
#             "username": TextInput(attrs={
#                 "id": "input-name",
#                 "class": "input",
#                 "placeholder": "Имя пользователя"
#             }),
#             "email": EmailInput(attrs={
#                 "id": "input-email",
#                 "class": "input",
#                 "placeholder": "Email",
#                 "type": "email"
#             }),
#             "password": TextInput(attrs={
#                 "id": "password-field",
#                 "class": "input",
#                 "placeholder": "Введите пароль",
#                 "type": "password"
#             })
#         }
#
#
# class LogInForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#         widgets = {
#             "username": TextInput(attrs={
#                 "id": "input-name",
#                 "class": "input",
#                 "placeholder": "Имя пользователя"
#             }),
#             "password": TextInput(attrs={
#                 "id": "password-field",
#                 "class": "input",
#                 "placeholder": "Введите пароль"
#             })
#         }
