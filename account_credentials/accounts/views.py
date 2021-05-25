from django.shortcuts import render, redirect, reverse
from .forms import CustomUserForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm


def home(request):
    return render(request, template_name='accounts/homepage.html')


# def register(request):
#     if request.method == "POST":
#         form = CustomUserForm(request.post)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             print("Registration Successful")
#             return redirect('accounts:home')
#     form = CustomUserForm
#     return render(request, template_name="accounts/register.html", context={"form": form})

class RegisterView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/register.html'

