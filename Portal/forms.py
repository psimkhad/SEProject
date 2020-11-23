from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))

    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Passsword', 'class': 'form-control'}))
