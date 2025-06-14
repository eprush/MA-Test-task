from fake_useragent import UserAgent
import requests
from requests import Response

from schemas import CookieSchema


def get_cookie(r: Response) -> str:
    cookie_string = r.headers["Set-Cookie"]
    cookie_string = cookie_string.split(";")
    return cookie_string[0][3:]

def get_data() -> CookieSchema:
    entry_url = "https://sentry.lenta.tech"
    entry_headers = {
        "Proxy-Authorization": "Basic",
        "Proxy-Connection": "keep-alive",
        "User-Agent": UserAgent(platforms="mobile").random
    }

    response = requests.get(entry_url, headers=entry_headers)
    if response.status_code != 200:
        raise ValueError(f"Invalid status code: {response.status_code}")
    h = response.headers
    result = {
        "content_type": h["Content-Type"],
        "connection": h["Connection"],
        "vary": h["Vary"],
        "cookie": get_cookie(response),
    }
    return CookieSchema(**result)

def parse_data(*args):
    ...

def save_parsed_data(*args):
    ...

def main():
    data = get_data()
    parsed_data = parse_data(data)
    save_parsed_data(parsed_data)
    ...

if __name__ == "__main__":
    data = get_data()
    print(data)
