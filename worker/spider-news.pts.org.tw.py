#!/usr/bin/env python3

def main():
    url = 'https://news.pts.org.tw/dailynews.php'
    res = requests.get(url)

    html = lxml.html.fromstring(res.text)

if '__main__' == __name__:
    main()
