import requests
import pandas as pd
import datetime


def check_input():
    st_date = input("Please input start date. Example: 2021/12/01\nstart date: ")
    end_date = input("Please input end date. Example: 2022/01/22\nend date: ")

    try:
        st_date_obj = datetime.datetime.strptime(st_date, "%Y/%m/%d")
        end_date_obj = datetime.datetime.strptime(end_date, "%Y/%m/%d")
        if end_date_obj > st_date_obj:
            return st_date, end_date
        else:
            print("The input end date is smaller than start date. Please try again. \n")

    except ValueError:
        print("The input dates are not valid or does not have correct format. Please try again. \n")


def main():
    st_date, end_date = check_input()

    site = "https://cn.investing.com/instruments/HistoricalDataAjax"
    payload = {"curr_id": "6408", "smlID": "1159963", "header": "AAPL历史数据", "st_date": st_date, "end_date": end_date, "interval_sec": "Daily", "sort_col": "date", "sort_ord": "DESC", "action": "historical_data"}
    headers = {"content-type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41", "x-requested-with": "XMLHttpRequest"}
    response = requests.post(url=site, headers=headers, data=payload)

    df = pd.read_html(response.text)[0]
    return df.to_json(orient='index', force_ascii=False)


if __name__ == '__main__':
    main()


