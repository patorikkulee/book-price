import requests
from bs4 import BeautifulSoup as bs

keyword = "民法"
url = f'http://www.angle.com.tw/search.asp?keyword={keyword}&col=1'
page = requests.get(url)

soup = bs(page.text, "html.parser")
print(soup.find_all('tr'))

# items = soup.find("table", {"id": "itemlist_table"})
# prices = items.find("")