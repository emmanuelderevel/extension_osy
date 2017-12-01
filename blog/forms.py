from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'password'}))
