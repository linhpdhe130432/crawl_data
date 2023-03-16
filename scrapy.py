import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
soup = BeautifulSoup(response.content, "html.parser")
print(soup)