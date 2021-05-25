from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login


def home(request):
    return render(request, template_name='accounts/homepage.html')


def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("Registration Successful")
            return redirect('accounts:home')
    form = CustomUserForm
    return render(request, template_name="accounts/register.html", context={"form": form})


