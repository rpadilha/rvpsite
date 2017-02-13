from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(label='Email', max_length=60)
    password = forms.CharField(label='Senha', max_length=12, widget=forms.PasswordInput())