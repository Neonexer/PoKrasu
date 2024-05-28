from django.contrib.auth.forms import UserCreationForm

from .models import User
from django.forms import ModelForm, TextInput, EmailInput

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

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
            }),
            "password": TextInput(attrs={
                "id": "password-field",
                "class": "input",
                "placeholder": "Введите пароль",
                "type": "password"
            })
        }


class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            "username": TextInput(attrs={
                "id": "input-name",
                "class": "input",
                "placeholder": "Имя пользователя"
            }),
            "password": TextInput(attrs={
                "id": "password-field",
                "class": "input",
                "placeholder": "Введите пароль"
            })
        }

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User