from bs4 import BeautifulSoup
from urllib.request import urlopen

url = input("Enter the URL : ")

page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

print(soup)