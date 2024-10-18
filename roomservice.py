import os
import requests
from bs4 import BeautifulSoup




# Telegram Bot 설정 secrets.TELEGRAM_TOKEN
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# 크롤링할 URL
url = 'https://www.seocho.go.kr/site/ta/ex/tean/TeanFCalendar.do'

def send_telegram_message(message):
    """Telegram API를 사용하여 메시지를 전송하는 함수"""
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(telegram_url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def check_room_availability():
    """방의 예약 가능 여부를 확인하는 함수"""
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        messages = []  # 메시지를 저장할 리스트
        
        # 각 방이 포함된 td를 찾아서 처리
        tds = soup.find_all('td', class_='sat')  # 토요일 기준으로 필터링
        for td in tds:
            # 날짜(span.num)를 먼저 찾음
            date_span = td.find('span', class_='num')
            if date_span and date_span.text.strip():  # 날짜가 존재하는지 확인
                date = date_span.text.strip()  # 날짜 추출 (예: 26)
                
                # 방 정보를 포함한 a 태그들 찾기
                links = td.find_all('a')
                for link in links:
                    room_type = link.text.strip()
                    if '4인실(온돌)' in room_type or '4인실(침대)' in room_type:
                        availability = int(room_type.split('(')[-1].split(')')[0])  # 예약 가능 수 파싱
                        if availability >= 0:
                            # 메시지 형식: "26일 - 4인실(온돌) - (2)"
                            message = f"{date}일 - {room_type.split('(')[0]} - ({availability})"
                            messages.append(message)  # 메시지를 리스트에 추가

        if messages:
            # 리스트의 메시지를 엔터로 구분하여 하나의 문자열로 묶음
            full_message = "\n".join(messages)
            send_telegram_message(full_message)
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

if __name__ == '__main__':
    # 채팅 ID가 없으면 getUpdates로 채팅 ID를 확인하는 절차 추가
    if CHAT_ID == 'YOUR_CHAT_ID':
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        response = requests.get(telegram_url)
        data = response.json()
        print(data)  # 여기서 채팅 ID를 확인 후 변수에 저장하여 사용
    else:
        check_room_availability()
