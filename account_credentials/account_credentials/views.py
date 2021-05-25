from django.shortcuts import render


def redirect_home(request):
    return render(request, template_name="accounts/homepage.html")
