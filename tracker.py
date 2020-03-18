from datetime import date
from send_email import send_email
from data import search_api, load_keywords
import requests
import csv
from os import path

SERP_API = search_api()

KEYWORDS = load_keywords()
# Enter the Domain that you want to track without http:// or www
IDENTIFIER = "motadata.com"

dataset = []


def main():
    for key in KEYWORDS:
        tracker(key.strip())
    if len(dataset):
        filename = f"SERP_Rank_Report_{date.today().__str__()}.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as w_file:
            header = dataset[0].keys()
            writer = csv.DictWriter(w_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(dataset)
    if path.isfile(filename):
        print(send_email(filename))


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
                    dataset.append({
                        'Keyword': keyword,
                        'Position': obj['position'],
                        'Title': obj['title'],
                        'URL': obj['url']
                    })
            except:
                print(f"Error in Fetching data for {keyword}")
                continue
    except:
        print("Response Error")


if __name__ == "__main__":
    main()
