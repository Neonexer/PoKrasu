from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from .models import User
from django.forms import ModelForm, TextInput, EmailInput
# from django.contrib.auth.models import User
from .models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput, Textarea, FileInput


# Create a User
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput(attrs={
        'id': 'password-field',
        'class': 'input',
        'placeholder': 'Введите пароль',
    }))

    password2 = forms.CharField(widget=PasswordInput(attrs={
        'id': 'password-field2',
        'class': 'input',
        'placeholder': 'Повторите пароль',
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
                    "username": TextInput(attrs={
                        "id": "input-name",
                        "class": "input",
                        "placeholder": "Имя пользователя"
                    }),
                    "email": EmailInput(attrs={
                        "id": "input-email",
                        "class": "input",
                        "placeholder": "Email",
                        "type": "email"
                    })
                }


# Authenticate a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'id': 'input-name',
        'class': 'input',
        'placeholder': 'Имя пользователя',
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'id': 'password-field',
        'class': 'input',
        'placeholder': 'Введите пароль',
    }))


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'city', 'about', 'img')

        widgets = {
            "first_name": TextInput(attrs={
                "id": "name",
            }),
            "username": TextInput(attrs={
                "id": "username"
            }),
            "email": EmailInput(attrs={
                "id": "email"
            }),
            "city": TextInput(attrs={
                "id": "city"
            }),
            "about": Textarea(attrs={
                "id": "about"
            }),
            "img": FileInput(attrs={
                "id": "photo-input",
                "accept": "image/*",
                "onchange": "loadPhoto(event)",
                "style": "display: none;"
            })
        }


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
