from django import forms
from .models import User
from django.contrib.auth import authenticate, login

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("user_name", "first_name", "last_name", "email", "password", "balance", "image")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        #user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
