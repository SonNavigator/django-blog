from django import forms 
from .models import Contact

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject',
                  'email',
                  'sender',
                  'detail'
                ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	      model = User
	      fields = ["username", "email", "password1", "password2"]