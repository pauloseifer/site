import requests
from bs4 import BeautifulSoup

url = input("Site: ")

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

arquivo = open("links.txt", "w")

urls = []
for link in soup.find_all('a'):
    href = link.get("href")
    descricao = link.text
    arquivo.write("href = " + href + "\n")
    arquivo.write("descricao = " + descricao + "\n")

arquivo.close()
