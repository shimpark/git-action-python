import os
from datetime import datetime
from pytz import timezone
from crawling_yes24 import parsing_beautifulsoup, extract_book_data
# from crawling_interpack import parsing_interpark_beautifulsoup, extract_interpark_book_data
# from crawling_kyobo import parsing_kyobo_beautifulsoup, extract_kyobo_book_data
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")

    yes24_it_new_product_url = "https://www.yes24.com/Product/Category/NewProduct?categoryNumber=001001003&pageNumber=1&pageSize=120&newProductType=NEW"
    # interpark_it_new_product_url = "http://book.interpark.com/display/DisplayNewBook.do?_method=newBookList&sc.shopNo=0000400000&sc.dispNo=028023&bid1=NewBook&bid2=Category&bid3=Kor_Book&bid4=028023"
    # kyobo_it_new_product_url = "https://product.kyobobook.co.kr/category/KOR/3315#?page=1&type=all&sort=new"

    soup_yes24 = parsing_beautifulsoup(yes24_it_new_product_url)
    issue_yes24_title = f"YES24 IT 신간 도서 알림({today_data})"
    issue_yes24_content = extract_book_data(soup_yes24)
    
    """
    soup_kyobo = parsing_kyobo_beautifulsoup(kyobo_it_new_product_url)
    issue_kyobo_title = f"교보문고 IT 신간 도서 알림({today_data})"
    upload_kyobo_contents = extract_kyobo_book_data(soup_kyobo)
    """
    
    
    
    
    """
    soup_interpark = parsing_interpark_beautifulsoup(
        interpark_it_new_product_url)
    issue_interpark_title = f"인터파크 IT 신간 도서 알림({today_data})"
    issue_interpark_content = extract_interpark_book_data(soup_interpark, 'https://book.interpark.com')
    """
    
    """
    soup_kyobo = parsing_kyobo_beautifulsoup(kyobo_it_new_product_url)
    issue_kyobo_title = f"교보문고 IT 신간 도서 알림({today_data})"
    issue_kyobo_content = extract_kyobo_book_data(soup_kyobo)
    """   

    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "git-action-python"

    repo = get_github_repo(access_token, repository_name)

    upload_github_issue(repo, issue_yes24_title, issue_yes24_content)
    
    # upload_github_issue(repo, issue_interpark_title, issue_interpark_content)
    # upload_github_issue(repo, issue_kyobo_title, issue_kyobo_content)

    print("Upload Github Issue Success!")

