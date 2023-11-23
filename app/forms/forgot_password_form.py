from django import forms

from app.models import User


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email not found')
        return email


