from django import forms
from .models import Contact, Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']



        