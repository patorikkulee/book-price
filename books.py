import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


class book:
    pass

keyword = "民法"
url = f'https://search.books.com.tw/search/query/key/{keyword}/cat/all'
page = requests.get(url)
soup = bs(page.text, "html.parser")

dom = etree.HTML(str(soup))
print(dom.xpath('/html/body/div[6]/div/div/div/div[5]'))

'''
items = soup.find("table", {"id": "itemlist_table"})
print(items)
names = [x.text for x in items.find_all("a", rel="mid_name")]

info = items.find_all("li")
for i in range(len(info)//2):
    print(info[i].text , '---')

'''

