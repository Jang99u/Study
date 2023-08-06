# https://auto-trading.tistory.com/entry/%ED%8A%B9%EA%B0%95-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81Web-Crowling-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90%EA%B3%BC-%EC%BD%94%EB%93%9C-%EA%B5%AC%ED%98%84with-Python

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EA%B5%AD+%EA%B0%9C%EC%9D%B8%EC%86%8C%EB%B9%84%EC%A7%80%EC%B6%9C%EB%AC%BC%EA%B0%80")
soup = bs(html, "html.parser")

value = soup.find("strong", {"class" : "num"})
print(value)

value = value.text.strip()
print(value)