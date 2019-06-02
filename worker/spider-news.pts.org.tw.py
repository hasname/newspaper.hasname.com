#!/usr/bin/env python3

import lxml.html
import requests

def main():
    url = 'https://news.pts.org.tw/dailynews.php'
    res = requests.get(url)

    html = lxml.html.fromstring(res.text)
    for art in html.cssselect('a[href^="https://news.pts.org.tw/article/"]'):
        article_url = art.get('href')
        parse_url(article_url)

def parse_url(url):
    res = requests.get(url)
    html = lxml.html.fromstring(res.text)

if '__main__' == __name__:
    main()
