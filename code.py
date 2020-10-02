import requests 
from bs4 import BeautifulSoup
search="weather in "+input("enter the location")
url=f"https://www.google.com/search?&q={search}"
r=request.get(url)
s=BeautifulSoup(r.text,"html.parser")
print(s.find("div",class_="BNeawe").text)

