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
url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR'
output_path = '0. 미디어 데이터 협업 및 활용하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/1-prepare'
output_path = '1. 실습 유의사항 및 준비.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/1-prepare/workshopstudio'
output_path = '1-1. Workshop Studio 이벤트로 시작하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/2-datacollaboration'
output_path = '2. 데이터 협업하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/2-datacollaboration/a-understandingdata'
output_path = '2-1 (옵션) 데이터 이해하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/2-datacollaboration/b-collaboration'
output_path = '2-2 공동 작업(Collaboration) 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/2-datacollaboration/c-tableconfiguration'
output_path = '2-3 구성된 테이블(ConfiguredTable) 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/2-datacollaboration/d-query'
output_path = '2-4 연결된 테이블에 쿼리하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy'
output_path = '3. 차등 프라이버시.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/a-collaboration'
output_path = '3-1 공동 작업(Collaboration) 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/b-configuredtables'
output_path = '3-2 구성된 테이블(Configured Table) 생성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/c-analysisrule'
output_path = '3-3 분석 규칙(Analysis Rule) 구성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/d-associateconfiguredtable'
output_path = '3-4 구성된 테이블(Configured Table) 공동 작업에 연결하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/e-differentialprivacy'
output_path = '3-5 차등 프라이버시(Differential Privacy) 설정 구성하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/3-differentialprivacy/f-queryexecution'
output_path = '3-6 파트너(Newsnow) 계정에서 차등 프라이버스 기반 집계 쿼리 실행하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/0814249c-a5fc-4342-bc2a-93d5007f1150/ko-KR/summary'
output_path = '4. 리소스 정리하기.pdf'
generate_pdf(url, output_path)

