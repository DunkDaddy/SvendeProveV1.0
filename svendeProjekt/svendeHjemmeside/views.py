import json
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, RegistreringsForm, PasswordForm, EmailForm
from svendeORMAndAPI.models import *
import requests

# Create your views here.
headers = {'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Authorization': 'Token 86839eb173ab3783f76b3a431e6c1a3ce9f47029'}

bruger = ''
x = 0
fail = ''


def base(response):
    login = LoginForm
    registrering = RegistreringsForm
    return render(response, 'base.html', {"login": login, "registrering": registrering, 'fail': fail})


def home(response):
    p = PasswordForm
    e = EmailForm
    billeder = Billeder.objects.all()
    kategorier = Kategori.objects.all()
    return render(response, 'Homepage.html', {'bruger': bruger, 'billeder': billeder, 'kategorier': kategorier, 'valgtKategori': x, 'email': e, 'password': p})


def startpage(response):
    if response.method == "POST":
        registrering = RegistreringsForm(response.POST)
        if registrering.is_valid():
            brugernavn = registrering.cleaned_data['brugernavn']
            data = {'brugernavn': f'{brugernavn}'}
            url = 'http://127.0.0.1:8000/data/BC/'
            request = requests.post(url, data=json.dumps(data), headers=headers)
            response_json = request.json()
            if not response_json:
                navn = registrering.cleaned_data['navn']
                password = registrering.cleaned_data['password']
                email = registrering.cleaned_data['email']
                data = {'navn': f'{navn}', 'brugernavn': f'{brugernavn}', 'password': f'{password}', 'email': f'{email}'}
                url = 'http://127.0.0.1:8000/data/BrugerCreate/'
                request = requests.post(url, data=json.dumps(data), headers=headers)
                response_json = request.json()
                if response_json:
                    return base(response)
                else:
                    return base(response)
            else:
                login = LoginForm
                registrering = RegistreringsForm
                global fail
                fail = 'Brugernavn eksitere allerede'
                return base(response)

        login = LoginForm(response.POST)
        if login.is_valid():
            brugernavn = login.cleaned_data['brugernavn']
            password = login.cleaned_data['password']
            data = {'brugernavn': f'{brugernavn}', 'password': f'{password}'}
            url = 'http://127.0.0.1:8000/data/PC/'
            request = requests.post(url, data=json.dumps(data), headers=headers)
            response_json = request.json()
            if response_json:
                global bruger
                bruger = Bruger.objects.get(brugernavn=brugernavn)
                return home(response)
            else:
                fail = 'Forkert Brugernavn eller Password'
                return base(response)

        password = PasswordForm(response.POST)
        if password.is_valid():
            bruger.password = make_password(password.cleaned_data['password'])
            bruger.save()
            return home(response)

        email = EmailForm(response.POST)
        if email.is_valid():
            bruger.email = email.cleaned_data['email']
            bruger.save()
            return home(response)

        if response.method == "POST":
                try:
                    global x
                    x = response.POST['id']
                    x = int(x)
                    return home(response)
                finally:
                    try:
                        billedet = Billeder.objects.get(id=int(response.POST['billed']))
                        billedet.delete()
                        return home(response)
                    except:
                        return home(response)

    else:
        return base(response)
