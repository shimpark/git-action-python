import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parsing_interpark_beautifulsoup(url):
    """
    뷰티풀 수프로 URL에서 HTML을 파싱하는 함수.
    :param url: 파싱할 URL
    :return: BeautifulSoup 객체
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공했는지 확인
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_interpark_book_data(soup, base_url):
    """
    BeautifulSoup 객체에서 책 데이터를 추출하는 함수.
    :param soup: BeautifulSoup 객체
    :param base_url: 사이트의 기본 URL
    :return: HTML 형식의 책 정보 문자열
    """
    if soup is None:
        return "Error: Unable to fetch data from the website."

    upload_contents = ''
    new_books = soup.select(".displayWrap")

    for new_book in new_books:
        # 제목 추출
        title_tag = new_book.select_one("div.infoWrap p.inc_tit a b")
        book_name = title_tag.text if title_tag else "Unknown Title"

        # URL 추출 및 절대 경로 생성
        link_tag = new_book.select_one("div.infoWrap p.inc_tit a")
        url_suffix = link_tag['href'] if link_tag else "#"
        url = urljoin(base_url, url_suffix)

        # 가격 추출
        price_tag = new_book.select_one("div.infoWrap p.inc_price span.FnowCoupon b.nowMoney")
        price = price_tag.text.strip() if price_tag else "Unknown Price"

        # 콘텐츠 포맷팅
        content = f"<a href='{url}'>{book_name}</a>, {price}<br/>\n"
        upload_contents += content

    return upload_contents
