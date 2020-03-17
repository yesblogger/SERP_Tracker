from send_email import send_email
from data import search_api, load_keywords
import requests

SERP_API = search_api()

KEYWORDS = load_keywords()
# Enter the Domain that you want to track without http:// or www
IDENTIFIER = "motadata.com"


def main():
    for key in KEYWORDS:
        tracker(key.strip())


def tracker(keyword):
    params = {
        'access_key': SERP_API,
        'query': keyword,
        "num": 100,
        "gl": 'in'
    }

    api_response = requests.get(
        'http://api.serpstack.com/search', params=params).json()

    try:
        for obj in api_response['organic_results']:

            try:
                if IDENTIFIER in obj['domain']:
                    position = obj['position']
                    url = obj['url']
                    send_email(keyword, position, url)
            except:
                continue
    except:
        print("Response Error")


if __name__ == "__main__":
    main()
