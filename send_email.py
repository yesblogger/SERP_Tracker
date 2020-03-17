import requests
from data import email_api

API = email_api()  # Past your mailgun api here instead of function


def send_email(keyword, position, url):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox4285061f779240d7bfe55a39e0e1bda0.mailgun.org/messages",
        auth=("api", API),
        data={"from": "SERP Extractor <mailgun@sandbox4285061f779240d7bfe55a39e0e1bda0.mailgun.org>",
              "to": ["amartyazzz@gmail.com"],
              "subject": "SERP ALERT",
              "text": f'''
              
              Hi,

              Motadata has appeared on position: {position} for the keyword: {keyword}. The url
              of the post {url}
              
              '''})
