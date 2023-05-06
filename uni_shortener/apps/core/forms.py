from django import forms
from uni_shortener.apps.core import models


class ShortenedURLCreationForm(forms.ModelForm):
    url = forms.CharField(label="", max_length=255, widget=forms.URLInput(attrs={
        "class": "form-control",
        "placeholder": "Enter a link to shorten it"
    }))

    class Meta:
        model = models.ShortenedURL
        fields = ["url"]


class ShortenedURLSearchForm(forms.Form):
    hash = forms.CharField(label="", max_length=6, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter a shortened link hash"
    }))
