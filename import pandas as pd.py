import requests
from bs4 import BeautifulSoup
import webbrowser

# 검색어를 입력 받습니다.
query = input("검색어를 입력하세요: ")

# 시작 날짜와 종료 날짜를 입력 받습니다.
start_date = input("시작 날짜를 입력하세요 (예: 2022-01-01): ")
end_date = input("종료 날짜를 입력하세요 (예: 2022-12-31): ")

# 검색어와 날짜를 URL 인코딩합니다.
query = requests.utils.quote(query)
start_date = requests.utils.quote(start_date)
end_date = requests.utils.quote(end_date)

# 검색 결과를 가져올 URL 주소를 생성합니다.
url = f"https://search.naver.com/search.naver?where=news&query={query}&ds={start_date}&de={end_date}"

# 웹 페이지에 요청을 보내고 응답을 받아옵니다.
response = requests.get(url)

# 응답의 내용을 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 제목과 링크를 추출합니다.
articles = soup.select('.news_tit')

if articles:
    for article in articles:
        title = article.text
        link = article['href']
        print(title)
        print(link)
        print()

        # 기사 페이지로 이동합니다.
        webbrowser.open(link)
else:
    print("검색 결과가 없습니다.")
