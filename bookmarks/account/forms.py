from django import forms


class LoginForm(forms.Form):
    """Login form for the user."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
