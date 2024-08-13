import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup.title)
print(soup.title.string)