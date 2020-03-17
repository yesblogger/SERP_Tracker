def search_api():
    with open("search_api.txt", mode='r') as r_file:
        return r_file.readline().strip()


def email_api():
    with open("email_api.txt", mode='r') as r_file:
        return r_file.readline().strip()


def load_keywords():
    with open("keywords.txt", mode='r') as r_file:
        return r_file.readlines()
