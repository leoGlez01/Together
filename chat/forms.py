from django import forms


class FormLogin(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    