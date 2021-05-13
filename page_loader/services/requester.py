import requests


def get_response(url):
    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()
    return response
