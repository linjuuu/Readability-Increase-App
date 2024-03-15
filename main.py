# from get_all_tag import GetAllTag


# url = 'https://blog.naver.com/hahehe-/223371140368'

# get_all_tag = GetAllTag(url)
# get_all_tag.do()


from selenium import webdriver
import time


# 크롬 드라이버 경로 설정 (다운로드한 드라이버의 경로로 수정)
chromedriver_path = '/Users/jun1/Downloads/chromedriver-mac-arm64/chromedriver'

# 셀레니움 웹 드라이버 실행
driver = webdriver.Chrome(chromedriver_path)

# 웹 페이지의 URL
url = 'https://blog.naver.com/hahehe-/223371140368'

# 해당 URL 열기
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기 (예: 5초)
time.sleep(5)

# 페이지의 텍스트 추출
page_text = driver.find_element_by_tag_name('body').text

print(page_text)

# 웹 드라이버 종료
driver.quit()
