# myapp/forms.py

from django import forms

class LoginPage(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
