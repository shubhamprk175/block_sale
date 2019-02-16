from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "email", "balance", "image")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
