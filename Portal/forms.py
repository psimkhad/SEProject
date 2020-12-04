from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))

    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Passsword', 'class': 'form-control'}))


class RegisterForm(forms.Form):

    ROLES = [
        ('ADMIN', 'Admin'),
        ('FINANCE_ADMIN', 'Finance Admin'),
        ('SALES_ADMIN', 'Sales Admin'),
        ('HR_ADMIN', 'HR Admin'),
        ('TECH_ADMIN', 'Tech Admin'),
    ]

    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))

    userrole = forms.CharField(required=True, label='',
                               widget=forms.Select(choices=ROLES, attrs={'class': 'form-control'}))

    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Passsword', 'class': 'form-control'}))

    confirm_password = forms.CharField(required=True, label='',
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Passsword', 'class': 'form-control'}))
