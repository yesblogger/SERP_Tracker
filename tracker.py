from datetime import date
from data import search_api_key, load_keywords
from location import geo_code
import requests
import csv

# GLOBAL VARIABLES
SERP_API_LIST = search_api_key() # list of apis

CALL_COUNTER = len(SERP_API_LIST)

SERP_API = ""

KEYWORDS = load_keywords()  # points a list of keywords to the variable

DATASET = []

IDENTIFIER = None

LOCATION = None

# FUNCTIONS


def main():
    global IDENTIFIER, LOCATION
    # Setting the remaining two global variables
    IDENTIFIER = input(
        "Enter the Domain that you want to track; e.g. domain.com: ").strip()
    while True:
        LOCATION = geo_code(input("Enter Country for the SERP: ").strip())
        if LOCATION != "":
            break
    # Fetching the SERP data
    for key in KEYWORDS:
        tracker(key.strip())
    # writing SERP data into a csv file
    if len(DATASET):
        filename = f"SERP_Rank_Report_{date.today().__str__()}.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as w_file:
            header = DATASET[0].keys()
            writer = csv.DictWriter(w_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(DATASET)


def tracker(keyword):
    # Setting parameters for API call
    params = {
        'access_key': SERP_API,
        'query': keyword,
        "num": 100,
        "gl": LOCATION
    }

    # feting json content from the api
    api_response = requests.get(
        'http://api.serpstack.com/search', params=params).json()

    try:
        for obj in api_response['organic_results']:

            try:
                if IDENTIFIER in obj['domain']:
                    DATASET.append({
                        'Keyword': keyword,
                        'Position': obj['position'],
                        'Title': obj['title'],
                        'URL': obj['url']
                    })
                    break
            except:
                print(f"Error in Fetching data for {keyword}")
                continue
    except:
        # if SERP data is not returned then it will give response error
        print("Response Error")


if __name__ == "__main__":
    main()
