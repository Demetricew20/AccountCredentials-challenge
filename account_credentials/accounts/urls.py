from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.user_login, name='login')
]
