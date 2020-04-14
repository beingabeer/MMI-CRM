from django.forms import ModelForm
from .models import Order
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': _("Password")}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': _("Password Confirm")}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
