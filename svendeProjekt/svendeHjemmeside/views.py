import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import LoginForm, RegistreringsForm
from svendeORMAndAPI.models import *
import requests

# Create your views here.
headers = {'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Authorization': 'Token 86839eb173ab3783f76b3a431e6c1a3ce9f47029'}

bruger = ''
def base(response):
    login = LoginForm
    registrering = RegistreringsForm
    return render(response, 'base.html', {"login": login, "registrering": registrering})


def home(response):
    billeder = Billeder.objects.all()
    kategorier = Kategori.objects.all()
    return render(response, 'Homepage.html', {'bruger': bruger, 'billeder': billeder, 'kategorier': kategorier})


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
                return render(response, 'base.html', {"login": login, "registrering": registrering, 'fail': 'Brugernavn eksitere allerede'})

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
                login = LoginForm
                registrering = RegistreringsForm
                return render(response, 'base.html',{"login": login, "registrering": registrering, "fail": 'Forkert Brugernavn eller Password'})
    else:
        return base(response)
