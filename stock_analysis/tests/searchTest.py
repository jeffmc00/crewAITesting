import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search"
params = {"q": "Latest AI News"}

response = requests.get(url, params=params)

soup = BeautifulSoup(response.content, 'html.parser')
print (soup)
results = soup.find_all("div", class_="g")
for result in results:
    print(result)


