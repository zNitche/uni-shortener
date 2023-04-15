from django import forms
from core import models


class ShortenedURLCreationForm(forms.ModelForm):
    class Meta:
        model = models.ShortenedURL
        fields = ["url"]
