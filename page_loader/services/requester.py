import requests


def get_response(url):
    return requests.get(url, allow_redirects=False)
