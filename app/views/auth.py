from django.contrib.auth import logout
from django.shortcuts import render, redirect


def signup_view(request):
    return render(request, 'app/auth/signup.html')


def signin_view(request):
    return render(request, 'app/auth/signin.html')


def password_reset_view(request):
    return render(request, 'app/auth/password_reset.html')


def verify_email_view(request):
    return render(request, 'app/auth/verify_email.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def my_profile_view(request):
    return render(request, 'app/auth/my_profile.html')