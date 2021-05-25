from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import generic


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UpdateUserProfile(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(UpdateUserProfile, self).save(commit=False)
        if commit:
            user.save()
        return user

