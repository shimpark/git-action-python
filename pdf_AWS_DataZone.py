from playwright.sync_api import sync_playwright

def generate_pdf(url, output_path):
    with sync_playwright() as p:
        # 1. Chromium 브라우저를 실행합니다.
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 2. URL로 이동하여 페이지를 로드합니다.
        page.goto(url, wait_until='networkidle')

        # 3. 추가 대기 시간 (10초) - 페이지가 완전히 로드될 때까지 기다림
        page.wait_for_timeout(3000)  # 10000 밀리초 = 1초

        # 4. 페이지를 PDF로 저장합니다.
        page.pdf(
            path=output_path,
            format="A3",
            landscape=False,
            margin={"top": "20px", "bottom": "30px", "left": "20px", "right": "20px"}  # 여백 설정 추가
        )

        print(f"PDF 생성 완료: {output_path}")

        # 5. 브라우저를 닫습니다.
        browser.close()

# 사용 예시
url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR'
output_path = '0. Amazon DataZone 실습 (Basic).pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction'
output_path = '1. 소개.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction/target'
output_path = '1-1. 실습 대상자와 전제조건.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction/purpose'
output_path = '1-2. 실습의 목적.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction/services'
output_path = '1-3. 사용하는 AWS 서비스.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction/cost'
output_path = '1-4. 실습에서 발생하는 요금.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/introduction/important'
output_path = '1-5. 주의사항.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/flow'
output_path = '2.실습 전체 흐름.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on'
output_path = '3. 실습.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/login'
output_path = '3-1 실습 준비.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/rootdomain'
output_path = '3-2. Amazon DataZone 도메인과 데이터 포털 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/producer'
output_path = '3-3 생산자 프로젝트 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/environment'
output_path = '3-4 프로젝트 환경 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/data'
output_path = '3-5 DataZone에서 게시할 데이터 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/metadata'
output_path = '3-6 메타데이터 설정.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/publish'
output_path = '3-7 Amazon DataZone에서 데이터 게시.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/consumer'
output_path = '3-8 소비자 프로젝트 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/subscribe'
output_path = '3-9 게시된 데이터 자산을 소비자로 구독.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/approve'
output_path = '3-10 게시한 데이터에 대해 생산자가 소비자의 엑세스 승인.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/hands-on/analytics'
output_path = '3-11 데이터 생산자가 게시한 데이터 세트를 데이터 소비자가 Amazon Athena에서 분석.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete'
output_path = '4. 생성한 리소스 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete/datazone'
output_path = '4-1. Amazon DataZone 도메인 및 포털 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete/lakeformation'
output_path = '4-2. AWS Lake Formation 설정 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete/glue'
output_path = '4-3. AWS Glue Crawler 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete/iam'
output_path = '4-4. IAM 삭제.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a6d8f106-419c-4681-957b-5cf1fae973cc/ko-KR/delete/s3'
output_path = '4-5. Amazon S3 버킷 삭제.pdf'
generate_pdf(url, output_path)
