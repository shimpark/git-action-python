import requests
from bs4 import BeautifulSoup


def parsing_kyobo_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. 여기선 YES24 Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def extract_kyobo_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    new_books = soup.find_all("div", class_="detail")

    for new_book in new_books:

        book_name = new_book.select("div.title")[0].select("a")[
            0].select("strong")[0].text
        url_suffix = new_book.select("div.title")[0].select("a")[
            0].attrs['href']
        url = url_suffix

        price = new_book.select("strong.sell_price")[0].text

        content = f"<a href='{url}'>" + book_name + \
            "</a>" + ", " + price + "<br/>\n"
        upload_contents += content

    return upload_contents
