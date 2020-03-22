def search_api_key():
    with open("search_api.txt", mode='r') as r_file:
        return r_file.readline().strip()


def load_keywords():
    with open("keywords.txt", mode='r') as r_file:
        return r_file.readlines()  # returns a list of keywords from the file
