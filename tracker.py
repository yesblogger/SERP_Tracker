from datetime import date
from send_email import send_email
from data import search_api, load_keywords
import requests
import csv

SERP_API = search_api()

KEYWORDS = load_keywords()
# Enter the Domain that you want to track without http:// or www
IDENTIFIER = "motadata.com"

dataset = []


def main():
    today = date.today()
    with open(f"SERP_Rank_Report_{today.__str__()}.csv", mode='w', newline='', encoding='utf-8') as w_file:
        header = ['Keyword', 'Position', 'Title', 'URL']
        writer = csv.DictWriter(w_file, fieldnames=header)
        writer.writeheader()
        for key in KEYWORDS:
            tracker(key.strip())
        writer.writerows(dataset)


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
                    title = ['title']
            except:
                continue
            else:
                dataset.append({
                    'Keyword': keyword,
                    'Position': position,
                    'Title': title,
                    'URL': url
                })
    except:
        print("Response Error")


if __name__ == "__main__":
    main()
