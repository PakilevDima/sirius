from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import  forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class PaiForm(forms.ModelForm):

    card = forms.CharField(max_length=16, label='номер карты')  # любые данные



class SignUp(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'username', 'email', 'type_user']

class CustomUserLogin(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']