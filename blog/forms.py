from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
