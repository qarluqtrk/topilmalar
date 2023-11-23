from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView

from app.forms.login_form import LoginModelForm
from app.forms.register_form import RegisterModelForm
from app.forms.sendemail_form import send_email, send_forget_password_mail
from app.forms.token_form import account_activation_token
from app.models import User


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterModelForm(request.POST)
            if form.is_valid():
                form.save()
                send_email(form.data.get('email'), request, 'signup')
                messages.add_message(
                    request=request,
                    level=messages.WARNING,
                    message="Successfully send your email, please activate your profile"
                )
                return redirect('signup')
        else:
            form = RegisterModelForm()
    return render(request, 'app/auth/signup.html', {"form": form})


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginModelForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request=request,
                      user=user)
                return redirect('index')
        else:
            form = LoginModelForm()
    return render(request=request,
                  template_name='app/auth/signin.html',
                  context={"form": form})


class ActivateEmailView(TemplateView):
    template_name = 'app/auth/signup.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('signin')
        else:
            return HttpResponse('Activation link is invalid!')


class ActivatePasswordEmailView(TemplateView):
    template_name = 'app/auth/signup.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('change-password')
        else:
            return HttpResponse('Activation link is invalid!')


def forgot_password_view(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')

            if not User.objects.filter(email=email).first():
                messages.success(request, 'Not email found with this email.')
                return redirect('forgot_password')

            user = User.objects.get(email=email)
            send_forget_password_mail(email=user, request=request)
            messages.success(request, 'Successfully send your email, please change your password')
            return redirect('forgot_password')

    except Exception as e:
        print(e)
    return render(request,
                  'app/auth/forgot_password.html')


# def forgot_password_view(request):
#     return render(request, 'app/auth/forgot_password.html')


def verify_email_view(request):
    return render(request, 'app/auth/verify_email.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def my_profile_view(request):
    return render(request, 'app/auth/my_profile.html')
