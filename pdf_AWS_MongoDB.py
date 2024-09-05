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
url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR'
output_path = '1. MongoDB Atlas on AWS.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/setup'
output_path = '2. AWS 계정으로 워크샵 시작.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/mongodb-atlas-setup'
output_path = '3. MongoDB Atlas 프로비저닝.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/mongodb-atlas-setup/vpc-peering'
output_path = '3-1. (Optional) VPC Peering 설정.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task1-crud-and-mql'
output_path = '4. 실습1 - CRUD and MQL.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task1-crud-and-mql/1-lambda-custom-layer'
output_path = '4-1. Lambda Layer 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task1-crud-and-mql/2-lambda-function'
output_path = '4-2. Lambda Function 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task1-crud-and-mql/3-api-gateway'
output_path = '4-3. API Gateway 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task1-crud-and-mql/4-test'
output_path = '4-4. API 구현 테스트.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot'
output_path = '5. 실습2 - IoT.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot/1-mongodb-endpoint'
output_path = '5-1. MongoDB Endpoint 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot/2-amazon-data-firehose'
output_path = '5-2. Amazon Data Firehose 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot/3-test'
output_path = '5-3. Amazon Data Firehose 와 MongoDB 간의 연동 테스트하기.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot/4-mongodb-dashboard'
output_path = '5-4. MongoDB Dashboard 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task2-iot/5-mongodb-dashboard-share'
output_path = '5-5. MongoDB Dashboard 공유.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task3-eventbridge'
output_path = '6. 실습3 - Amazon EventBridge.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task3-eventbridge/1-mongodb-trigger'
output_path = '6-1. MongoDB Trigger 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task3-eventbridge/2-amazon-eventbridge'
output_path = '6-2. Amazon EventBridge 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/task3-eventbridge/3-test'
output_path = '6-3. MongoDB 와 Amazon EventBridge 간의 연동 테스트.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/a59b7b60-c327-41f2-9b73-81438196968a/ko-KR/clean-up'
output_path = '7. 리소스 정리.pdf'
generate_pdf(url, output_path)
