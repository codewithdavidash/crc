from django.contrib.auth.views import LoginView
from django.urls import path
from .forms import *
from . import views

app_name = 'core'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='auth/login.html', authentication_form=LoginForm), name='login'),
    path('accounts/settings/edit_profile/<str:pk>/', views.edit_profile, name='editProfile'),
    path('users-detail/<str:pk>/', views.users_detail, name='users_detail'),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('accounts/settings/', views.settings, name='settings'),
    path('accounts/logout/', views.LogoutView, name='logout'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('accounts/signup/', views.signup, name='signup'),
    path('academics/', views.academics, name='academics'),
    path('about/', views.about, name='about'),
    path('home/', views.index, name='index'),
    path('', views.landing, name='landing'),
]
