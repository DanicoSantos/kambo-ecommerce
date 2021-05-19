from django import forms
from django.forms import fields
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
                             'required': 'Sorry you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        users = UserBase.objects.filter(user_name=user_name)
        if users.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password_confirmation(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password_confirmation']:
            raise forms.ValidationError('Password do not match.')
        return cleaned_data['password_confirmation']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
