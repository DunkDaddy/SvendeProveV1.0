import requests

brugernavn = login.cleaned_data['brugernavn']
password = login.cleaned_data['password']
data = {'brugernavn': f'{brugernavn}', 'password': f'{password}'}
url = 'http://127.0.0.1:8000/data/PC/'

r = requests.post(url, data=json.dumps(data), headers=headers)