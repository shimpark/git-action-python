import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parsing_beautifulsoup(url):
    """
    BeautifulSoup를 사용하여 URL에서 HTML을 파싱하는 함수
    :param url: 파싱할 URL
    :return: BeautifulSoup 객체
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공적으로 완료되었는지 확인
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_book_data(soup):
    """
    BeautifulSoup 객체에서 책 데이터를 추출하는 함수
    :param soup: BeautifulSoup 객체
    :return: HTML 형식의 책 정보 문자열
    """
    if soup is None:
        return "Error: Unable to fetch data from the website."

    upload_contents = ''
    new_books = soup.select('#yesNewList li[data-goods-no]')
    base_url = "https://www.yes24.com"

    for new_book in new_books:
        # 제목과 링크 추출
        title_tag = new_book.select_one('a.gd_name')
        book_name = title_tag.text.strip() if title_tag else 'Unknown Title'
        url_suffix = title_tag['href'] if title_tag else '#'
        url = urljoin(base_url, url_suffix)

        # 가격 추출
        price_tag = new_book.select_one('.info_row.info_price em.yes_b')
        price = price_tag.text.strip() + "원" if price_tag else 'Unknown Price'

        # 콘텐츠 포맷팅
        content = f"<a href='{url}'>{book_name}</a>, {price}<br/>\n"
        upload_contents += content

    return upload_contents
