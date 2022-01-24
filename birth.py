import requests
import datetime
from bs4 import BeautifulSoup

def print_whichday(year, month, day) :
    r = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    aday = datetime.date(year, month, day)
    bday = aday.weekday()
    return r[bday]

def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

year = 2022

#일반 인증키(Encoding)
mykey = "WoMViKPOmQYKGqkJaAbyqMhjuTY0J%2B96EcUc5jWYLT76LbHMB3jma8vfyavnYsfFyi1sybZyivHy7Mt3qNQEfQ%3D%3D"

for month in range(1,13):

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'

    #공휴일 정보 조회
    operation = 'getRestDeInfo'
    params = {'solYear':year, 'solMonth':month}

    

    request_query = get_request_query(url, operation, params, mykey)
    get_data = requests.get(request_query)        

    if True == get_data.ok:
        soup = BeautifulSoup(get_data.content, 'html.parser')        
        #print(soup);
        item = soup.findAll('item')
        
        for i in item:
            
            day = int(i.locdate.string[-2:])
            weekname = print_whichday(int(year), int(month), day)
            print(i.datename.string, i.isholiday.string, i.locdate.string, weekname)                


