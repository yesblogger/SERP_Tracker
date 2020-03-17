import requests
from data import email_api

API = email_api()  # Past your mailgun api here instead of function


def send_email(file):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4285061f779240d7bfe55a39e0e1bda0.mailgun.org/messages",
        auth=("api", API),
        data={"from": "SERP Extractor <mailgun@sandbox4285061f779240d7bfe55a39e0e1bda0.mailgun.org>",
              "to": ["amartyazzz@gmail.com"],
              "subject": "SERP ALERT",
              "text": '''
              
              Hi,

              Your SERP rank report has been generated. Please find it attached with this email. 
              
              '''})
