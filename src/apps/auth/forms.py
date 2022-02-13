# apps/auth/forms.py

from apps.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# Custom User Creation form 
class UserCreationForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ), label="Email")
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ), max_length=155, label="Full Name")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ), label="Repeat Password")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already in use")
        
        return email
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords Don't Match")
        
        return password2
    
    def save(self, commit=True):
        new_user = User.objects.create_user(
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
            full_name = self.cleaned_data['full_name'],
        )
        return new_user
