from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin import widgets
from .models import User


class AddUserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email","first_name","username","last_name", "designation",)

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        widgets = {
            'designation': forms.TextInput(attrs={'type': 'hidden', },),
            'username': forms.TextInput(attrs={'readonly': True},),
        }
        fields = ("username", "email", "first_name", "last_name",
                  "designation") 
