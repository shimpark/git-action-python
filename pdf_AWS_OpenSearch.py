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
url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR'
output_path = '0. Centralized Logging with OpenSearch.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/100-introduction'
output_path = '1. 워크샵 소개.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/100-introduction/110-architecture-overview'
output_path = '1-1. 아키텍쳐 개요.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/100-introduction/120-aws-service-log-analytics-pipeline'
output_path = '1-2. AWS 서비스 로그 분석 파이프라인.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/100-introduction/130-app-log-analytics-pipeline'
output_path = '1-3. 애플리케이션 로그 분석 파이프라인.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/100-introduction/140-test-application'
output_path = '1-4. 테스트 애플리케이션 아키텍쳐.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/200-considerations'
output_path = '2. 고려 사항.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/200-considerations/210-cost'
output_path = '2-1. 비용.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/200-considerations/220-security'
output_path = '2-2. 보안.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/200-considerations/230-regions'
output_path = '2-3. 리전 선택.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/300-preparation'
output_path = '3. 환경 구성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/300-preparation/310-awsaccount'
output_path = '3-1. 고객 계정.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/300-preparation/330-workshopstudio'
output_path = '3-2. AWS 제공 계정 (Workshop studio).pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/400-deployment'
output_path = '4. 배포.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/400-deployment/410-solution-deployment'
output_path = '4-1 Centrailzied Logging with OpenSearch 솔루션 배포.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/400-deployment/420-test-app-deployment'
output_path = '4-2 테스트 애플리케이션 배포.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough'
output_path = '5. 실습.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/510-amazon-opensearch-service-domain'
output_path = '5-1 실습1 - Amazon OpenSearch 서비스 도메인 생성 및 임포트.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/512-access-proxy'
output_path = '5-2 실습2 - Access Proxy 생성.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/513-application-loadbalancer-log'
output_path = '5-3 실습3 - Application Loadbalancer 로그 수집.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/514-amazon-rds-log'
output_path = '5-4 실습4 - Amazon RDS 로그 수집.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/515-cloudfront-log'
output_path = '5-5 실습5 - Amazon CloudFront 로그 수집.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/516-waf-log'
output_path = '5-6 실습6 - WAF WebACL 접근 로그 수집.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/517-apache-http-server-log'
output_path = '5-7 실습7 - Apache HTTP Server 로그 수집.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/500-walkthrough/518-dashboard'
output_path = '5-8 실습8 - 대시보드 확인.pdf'
generate_pdf(url, output_path)

url = 'https://catalog.us-east-1.prod.workshops.aws/workshops/da5e674b-750a-47d5-a620-ea0b683d8728/ko-KR/600-clean-up'
output_path = '6. 실습 리소스 정리.pdf'
generate_pdf(url, output_path)

