from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .models import ContactUs,Assignment1


class RegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email',)

class Login(forms.Form):

        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

        def clean(self, *args, **kwargs):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError('This user does not exist')
                if not user.check_password(password):
                    raise forms.ValidationError('Password is incorrect')
                if not user.is_active:
                    raise forms.ValidationError('plus valide')
            return super(Login, self).clean(*args, **kwargs)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('',)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment1
        exclude = ('',)
