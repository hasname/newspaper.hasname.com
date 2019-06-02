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

    p = {}
    p.content = html.cssselect('.article_content')[0].text_content()
    p.title = html.cssselect('h2.article-title')[0].text_content()
    p.url = url

    tz = datetime.timezone(datetime.timedelta(hours=8))

    claimed_str = html.cssselect('.newscont-text h2')[0].text_content()
    ymd = re.match(r'(\d+)年(\d+)月(\d+)日', claimed_str)
    p.claimed_at = datetime.datetime(int(ymd[1]), int(ymd[2]), int(ymd[3]), tzinfo=tz).timestamp()

if '__main__' == __name__:
    main()
