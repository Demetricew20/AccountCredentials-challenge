from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm, UpdateUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User


def home(request):
    return render(request, template_name='accounts/homepage.html')


class RegisterView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Login successful!')
                return redirect('accounts:home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, template_name='accounts/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('accounts:home')


class ChangeUserPassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/update_password.html'


class ChangeProfile(generic.UpdateView):
    model = User
    form_class = UpdateUserProfile
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/update_profile.html'




