import tweepy
import json
from pprint import pprint

with open('keys.json') as key_file:
    data = json.load(key_file)

KEY = data["keys"]["consumer"]["key"]
SECRET = data["keys"]["consumer"]["secret"]
TOKEN = data["keys"]["access"]["token"]
T_SECRET = data["keys"]["access"]["secret"]

AUTH = tweepy.OAuthHandler(KEY, SECRET)
AUTH.set_access_token(TOKEN, T_SECRET)

API = tweepy.API(AUTH)


def make_query():
    global API
    string = input('Text or hashtags to search for: ')

    results = API.search(q=string, count=10)
    pprint(results)

def main():
    make_query()


if __name__ == "__main__":
    main()
