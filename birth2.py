import requests
from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def print_whichday(locdate) :    
    year = int(locdate[:4])  # 첫 4개 문자를 가져옵니다.
    month = int(locdate[4:6])  # 5번째와 6번째 문자를 가져옵니다.
    day = int(locdate[6:])  # 마지막 2개 문자를 가져옵니다.

    r = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    aday = datetime(year, month, day)
    bday = aday.weekday()
    return r[bday]

def getHoliday(year: int) -> pd.DataFrame:
    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
    api_key_utf8 = "RvVVDWYFt6W133cIk%2F8zdkX1Ppk23aCQvr%2B0RpAZk2hIQjaJzewdFOoY6xRr6mvJGlj%2BG19We6Fwmv5JwGwIlA%3D%3D"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "solYear": year,
        "numOfRows": 100
    }

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml-xml")
    items = xml.find('items')
    item_list = []

    if items is not None:  # items가 None이 아닌 경우에만 반복문 실행
        for item in items:
            item_dict = {
                "이름": item.find("dateName").text.strip(),
                "날짜": datetime.strptime(item.find("locdate").text.strip(), '%Y%m%d'),
                "요일": print_whichday(item.find("locdate").text.strip())
            }
            item_list.append(item_dict)

    return pd.DataFrame(item_list)

if __name__ == "__main__":
    holiday_df = getHoliday(2025)
    print(holiday_df)
