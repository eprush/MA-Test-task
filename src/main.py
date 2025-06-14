from fake_useragent import UserAgent
import requests
from requests import Response

from schemas import EntryResponseSchema

def raise_if_not_ok(r: Response):
    if r.status_code != 200:
        raise ValueError(f"Invalid status code: {r.status_code} with {r.url=}")


def get_data() -> EntryResponseSchema:
    headers = {
        "Proxy-Authorization": "Basic",
        "Proxy-Connection": "keep-alive",
        "User-Agent": UserAgent(platforms="mobile").random
    }
    entry_url = "https://sentry.lenta.tech"
    response = requests.get(entry_url, headers=headers)

    raise_if_not_ok(response)

    data_to_validate = {
        "content_type": response.headers["Content-type"],
        "connection": response.headers["Connection"],
        "vary": response.headers["Vary"],
        "cookie": response.cookies,
    }
    validated_data = EntryResponseSchema(**data_to_validate)

    second_url = "https://lentochka.lenta.com/"
    second_response = requests.get(second_url, headers=headers, cookies=validated_data.cookies.model_dump())

    raise_if_not_ok(second_response)
    return validated_data

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
