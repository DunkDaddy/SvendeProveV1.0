from django.forms import ModelForm
from django import forms
from svendeORMAndAPI.models import *
from django.forms import formset_factory


class RegistreringsForm(ModelForm):
    class Meta:
        model = Bruger
        fields = ('navn', 'brugernavn', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EmailForm(ModelForm):
    class Meta:
        model = Bruger
        fields = ('email',)


class PasswordForm(ModelForm):
    class Meta:
        model = Bruger
        fields = ('password',)


class LoginForm(ModelForm):
    class Meta:
        model = Bruger
        fields = ('brugernavn', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class KategoriForm(ModelForm):
    class Meta:
        model = Kategori
        fields = ('navn',)


class RapportForm(ModelForm):
    class Meta:
        model = Rapport
        fields = ('beskrivelse',)

