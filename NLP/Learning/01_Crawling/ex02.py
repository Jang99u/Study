# https://imomelet.tistory.com/18

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# ���� ��� ã��
html = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8")
soup = bs(html, "html.parser")

data = soup.find("span", {"class" : "scal temp"})
print(data)

data = data.text.strip()
print(data)

# �̼����� �� ã��
html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8")
soup = bs(html.text, "html.parser")

# d_news find & dd�� ��Ī�� ��� �� list��
data1 = soup.find("div", {"class" : "d_news"})
data2 = data1.findAll("dd")

dust = data2[0].find("span", {"class" : "atom2"}).text
print(dust)

# soup���� �ٷ� ã��
dust = soup.find("span", {"class" : "atom2"})
print(dust.text)