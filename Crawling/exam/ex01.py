from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EA%B5%AD+%EA%B0%9C%EC%9D%B8%EC%86%8C%EB%B9%84%EC%A7%80%EC%B6%9C%EB%AC%BC%EA%B0%80")
soup = bs(html, "html.parser")

value = soup.find("strong", {"class" : "num"})
print(value)

value = value.text.strip()
print(value)