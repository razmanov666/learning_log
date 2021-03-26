from django import forms
from .models import MyUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name','password']
        labels = {'text': '', 'password':''}
