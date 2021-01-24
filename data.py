import re

def search_api_key():
    apis = []
    with open("search_api.txt", mode='r') as r_file:
        for line in r_file.readlines():
            if re.match('.[^ ]', line):
                apis.append(line.strip())
        return apis

def load_keywords():
    keywords = []
    with open("keywords.txt", mode='r') as r_file:
        for key in r_file.readlines():
            if key != "\n":
                keywords.append(key.strip())
        return keywords  # returns a list of keywords from the file

if __name__ == "__main__":
    data = load_keywords()
    print(data)
    print(type(data))