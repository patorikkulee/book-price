import requests
from bs4 import BeautifulSoup as bs 
from book_info import *
import re

domain = 'https://sharing.com.tw/'
regex = r'.*！(\d+)元'

def search_sharing(keyword:str):
    url = f'https://sharing.com.tw/book_list_s.php?book_whit=0&book_data={keyword}&MM_update=form1'
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    items = soup.find_all("td", {"align": "left"})
    imgs = soup.find_all("td", {"align": "center"})

    item_list = []
    for i, img in list(zip(items, imgs)):
        name_block = i.find("td", {"class": "publishername"})
        name = name_block.text.lstrip('\n')
        link = domain + name_block.find("a")['href']

        publisher = i.find("td", {"class": "publisher"}).text.split('：')[-1]
        image = domain + img.find('img')['src']

        try:
            author = i.find("td", {"class": "publisher_au"}).text.split('：')[-1]
        except AttributeError:
            author = ""

        publish_date = ''
        price = discount_price = int()

        for j in i.find_all("td", {"class": "publishertype"}):
            info = j.text

            if '出版日' in info:
                publish_date = info.split('：')[-1]
            elif '定價' in info:
                price = info.split('：')[-1]
                price = int(price.rstrip('元'))
            elif '特價' in info:
                discount_price = re.search(regex, info.split('：')[-1]).group(1)
                if discount_price is None or discount_price=='':
                    discount_price = 0
                else:
                    discount_price = int(discount_price)
                
            print(type(price), type(discount_price))

        item_list.append(book('新學林', link, name, price, discount_price, author, publisher, publish_date, image=image))
    
    return item_list

test = booklist(search_sharing('民法'))
test = test.sort_price()

for i in test:
    print(i.lowest_price)
