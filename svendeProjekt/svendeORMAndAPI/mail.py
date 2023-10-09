import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
import json


sender_email = "svendeprojekt@gmail.com"
sender_password = "shhq oivw hdoy ooac"
subject = "Hello from Python"
body = "with image"



bruger_url = 'http://127.0.0.1:8000/data/BrugerListe/'
billed_url = 'http://127.0.0.1:8000/data/BillederListe/'
subscribed_url = 'http://127.0.0.1:8000/data/SubscribedListe/'

headers = {'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Authorization': 'Token 86839eb173ab3783f76b3a431e6c1a3ce9f47029'}


bruger_request = requests.get(bruger_url, headers=headers)
billed_request = requests.get(billed_url, headers=headers)
subscribed_request = requests.get(subscribed_url, headers=headers)


bruger_list = bruger_request.json()
billed_list = billed_request.json()
subscription_list = subscribed_request.json()
person = {'id': 0}
print(person['id'])
for subscription in subscription_list:
    for bruger in bruger_list:
        if subscription['bruger_id'] == bruger['id']:
            recipient_email = bruger['email']
            for billed in billed_list:
                if billed['kategori_id'] == subscription['kategori_id']:
                    billednavn = billed['billedet']
                    if person['id'] == bruger['id']:
                        pass
                    else:
                        with open(f'C:/Users/HFGF/Documents/GitHub/SvendeProveV1.0/svendeProjekt{billednavn}', 'rb') as f:
                            image_part = MIMEImage(f.read())
                        message = MIMEMultipart()
                        message['Subject'] = subject
                        message['From'] = sender_email
                        message['To'] = recipient_email
                        html_part = MIMEText(body)
                        message.attach(html_part)
                        message.attach(image_part)
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                            server.login(sender_email, sender_password)
                            server.sendmail(sender_email, recipient_email, message.as_string())
                        person = bruger