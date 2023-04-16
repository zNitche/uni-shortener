from django import forms
from core import models


class ShortenedURLCreationForm(forms.ModelForm):
    url = forms.CharField(label="", max_length=255, widget=forms.URLInput(attrs={
        "class": "form-control",
        "placeholder": "Enter a link to shorten it"
    }))

    class Meta:
        model = models.ShortenedURL
        fields = ["url"]

    form_template_name = "form.html"


class ShortenedURLSearchForm(forms.Form):
    hash = forms.CharField(label="", max_length=6, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter a shortened link hash"
    }))

    form_template_name = "form.html"
