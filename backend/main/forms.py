from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    your_name = forms.CharField(label="name", max_length=100)
    your_email = forms.EmailField(label="email", min_length=8)
    message = forms.CharField(label="message", max_length=510)