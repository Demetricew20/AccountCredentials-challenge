from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, template_name='accounts/homepage.html')


class RegisterView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:home')
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
    return render(request, template_name='accounts/login.html')


