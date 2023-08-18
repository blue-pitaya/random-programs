#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

default_favicon_url = "/images/default_favicon.png"
source_md_path = "bookmanrks.md"


def get_favicon(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    favicon_link = (
        soup.find("link", rel="icon")
        or soup.find("link", rel="shortcut icon")
        or soup.find("meta", attrs={"property": "og:image"})
    )
    favicon_url = favicon_link.get("href")

    return urljoin(url, favicon_url)


def parse_header(line):
    words = line.split(sep=" ")
    header_num = str(len(words[0]))
    header = " ".join(words[1:])
    print(f"<h{header_num}>{header}</h{header_num}>")


def get_favicon_element(url=default_favicon_url):
    return f'<img src="{url}" style="width: 16px; height: 16px;" />'


def parse_bookmark(line):
    words = line.split(sep=" ")
    url = words[0]
    title = " ".join(words[1:]).strip()
    favicon_element = get_favicon_element()
    try:
        favicon_url = get_favicon(url)
        favicon_element = get_favicon_element(favicon_url)
    except Exception:
        pass
    print(f'<a href="{url}">{favicon_element} {title}</a>')


if __name__ == "__main__":
    with open(source_md_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("http"):
                parse_bookmark(line)
            elif line.startswith("#"):
                parse_header(line)
            else:
                print("")
