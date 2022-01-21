import sys
import requests
from html.parser import HTMLParser
import json
import pandas as pd

close_prices = []
next_is_close = 0


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        global next_is_close
        if "年" in data and "月" in data and "日" in data and data.endswith("日"):
            next_is_close = 1
        if data.replace(".", "", 1).isdigit() and next_is_close == 1:
            close_prices.append(data)
            next_is_close = 0


def main():

    site = "https://cn.investing.com/equities/apple-computer-inc-historical-data"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
    response = requests.get(site, headers=headers)
    #
    # parser = MyHTMLParser()
    # parser.feed(response.text)
    #
    # print(json.dumps(close_prices))

    df = pd.read_html(response.text)[1]
    print(df['收盘'].to_json())


if __name__ == '__main__':
    main()


