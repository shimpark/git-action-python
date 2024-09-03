from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # GitHub Actions 환경에서 ChromeDriver 경로를 자동으로 찾습니다.
    driver_path = '/usr/bin/chromedriver'  # GitHub Actions에 기본 설치되는 경로

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def parsing_kyobo_beautifulsoup(url):
    """
    Selenium을 사용하여 동적으로 렌더링된 HTML을 가져와 BeautifulSoup로 파싱하는 함수
    :param url: 파싱할 URL
    :return: BeautifulSoup 객체
    """
    # Chrome 옵션 설정 (헤드리스 모드로 실행)
    options = Options()
    options.add_argument('--headless')  # 브라우저 UI 없이 실행
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Chrome WebDriver 경로 설정
    # driver_path = 'E:/github/git-shimpark/git-action-python/chromedriver.exe'  # 여기서 chromedriver 경로 수정
    # service = Service(executable_path=driver_path)

    driver = None
    try:
        # 브라우저 열기
        #driver = webdriver.Chrome(service=service, options=options)

        # github 작동
        driver = get_chrome_driver()
        driver.get(url)

        # 페이지가 로드될 시간을 기다림
        time.sleep(2)  # 필요에 따라 조정

        # 페이지 끝까지 스크롤하기
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 스크롤 후 페이지 로딩 시간 대기

            # 스크롤 후 페이지 높이 확인
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # 페이지 소스 가져오기
        html = driver.page_source

        # BeautifulSoup 객체 반환
        return BeautifulSoup(html, 'html.parser')

    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return None

    finally:
        if driver:
            driver.quit()  # 브라우저 닫기

def extract_kyobo_book_data(soup):
    """
    BeautifulSoup 객체에서 책 데이터를 추출하는 함수
    :param soup: BeautifulSoup 객체
    :return: HTML 형식의 책 정보 문자열
    """
    if soup is None:
        return "Error: Unable to fetch data from the website."

    upload_contents = ''
    new_books = soup.select('.prod_item')  # 각 책 항목을 포함하는 클래스 선택

    for new_book in new_books:
        # 제목과 링크 추출
        title_tag = new_book.select_one('a.prod_info')
        book_name = title_tag.select_one('span.prod_name').get_text(strip=True) if title_tag else 'Unknown Title'
        url = title_tag['href'] if title_tag else '#'

        # 가격 추출
        price_tag = new_book.select_one('div.prod_price span.price span.val')
        price = price_tag.get_text(strip=True) + "원" if price_tag else 'Unknown Price'

        # 콘텐츠 포맷팅
        content = f"<a href='{url}'>{book_name}</a>, {price}<br/>\n"
        upload_contents += content

    return upload_contents

