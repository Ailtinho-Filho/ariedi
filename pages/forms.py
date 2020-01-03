from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)