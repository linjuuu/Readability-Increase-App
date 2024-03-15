import requests
from bs4 import BeautifulSoup

class GetAllTag:
    def __init__(self,url):
        self.url = url
    
    def do(self):
        # 해당 URL에 GET 요청을 보냄
        response = requests.get(self.url)

        # HTML을 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # HTML 태그와 스크립트 태그 내의 텍스트 제거하고 출력
        for script in soup(["script", "style"]):
            script.decompose()

            text = soup.get_text()
            print(text)