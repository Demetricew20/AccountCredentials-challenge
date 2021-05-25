from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('update_password/', views.ChangeUserPassword.as_view(), name='update_password'),
    path('<int:pk>/update_profile/', views.ChangeProfile.as_view(), name='update_profile')
]
