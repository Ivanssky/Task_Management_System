from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from task_management_system.user.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'first_name', 'last_name']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'email', 'first_name', 'last_name', 'age']