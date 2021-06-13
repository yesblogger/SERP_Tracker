from datetime import date
from data import search_api_key, load_keywords
from location import geo_code
import requests
import csv

# GLOBAL VARIABLES
SERP_API_LIST = search_api_key() # list of apis

SERP_API = SERP_API_LIST.pop()

KEYWORDS = load_keywords()  # points a list of keywords to the variable

CALL_LIMIT = 0

DATASET = []

IDENTIFIER = None

LOCATION = None

# FUNCTIONS


def main():
    global IDENTIFIER, LOCATION
    # Setting the remaining two global variables
    call = 0
    # setting the local variable
    IDENTIFIER = input(
        "Enter the Domain that you want to track; e.g. domain.com: ").strip()
    CALL_LIMIT = int(input('Please enter the call limit for each API: ') or "{}".format(len(KEYWORDS)))
    while True:
        LOCATION = geo_code(input("Enter Country for the SERP: ").strip())
        if LOCATION != "":
            break
    # Fetching the SERP data
    for key in KEYWORDS:
        if call <= CALL_LIMIT:
            call += 1
            tracker(key.strip())
        else:
            if len(SERP_API_LIST):
                call = 0
                SERP_API = SERP_API_LIST.pop()
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

    # fetching json content from the api
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
