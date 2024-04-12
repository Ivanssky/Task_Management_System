from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_management_system.user.models import User


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'


        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['age'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['image'].label = ''


        self.help_texts = {}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'first_name', 'last_name', 'image']

        error_messages = {
            'password2': {
                'password_mismatch': "The two password fields didn't match.",
            },
            'password1': {
                'password_too_short': "Your password must contain at least 8 characters.",
                'password_common': "Your password is too common.",
                'password_entirely_numeric': "Your password can’t be entirely numeric.",
                'password_similar': "Your password can’t be too similar to your other personal information.",
            },
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'email', 'first_name', 'last_name', 'age']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'email', 'age']


class DeleteProfileForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirm', required=True)
