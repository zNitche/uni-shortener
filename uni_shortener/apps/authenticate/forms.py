from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, label="password", max_length=32)


class SecondFAForm(forms.Form):
    auth_code = forms.CharField(label="code", max_length=6, min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        auth_code = cleaned_data.get("auth_code")

        try:
            int(auth_code)

        except ValueError as e:
            raise forms.ValidationError("authentication code can contain only digits")
