import requests


def request(url, date):
    resp = requests.get('{}?date={}&api_key=DEMO_KEY'.format(url, date))
    print(resp.json())
    return resp


def request_img(url):
    resp = requests.get(url)
    return resp.content
