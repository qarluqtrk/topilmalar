from django import forms

from app.models import Item


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ()