import requests
from bs4 import BeautifulSoup as bs
from book_info import book
import sys, re

regex = r'^.* (\d+) 元$'
def preprocess_string(s:str):
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    s = s.replace('\xa0', ', ')
    return s

def search_books(keyword:str):
    url = f'https://search.books.com.tw/search/query/key/{keyword}/cat/all'
    page = requests.get(url)
    soup = bs(page.text, "html.parser")

    item_list = []

    items = soup.find("table", {"id": "itemlist_table"})
    names = [x.text for x in items.find_all("a", rel="mid_name")]
    links = ['https:'+x['href'] for x in items.find_all("a", rel="mid_name")]
    imgs = items.find_all('img', {"class": "b-lazy"})
    imgs = [i['data-srcset'].split('&')[0] for i in imgs]

    misc = items.find_all("li")
    for i in range(len(misc)//2):
        try:
            booktype, author, publisher, publish_date = [preprocess_string(x) for x in misc[2*i].text.split(',')]
        except:
            print([preprocess_string(x) for x in misc[2*i].text.split(',')])
        publish_date = publish_date.split(':')[-1]
        discount_price = misc[2*i+1].text.split(':')[-1]
        
        discount_price = int(re.search(regex, discount_price).group(1))
        item_list.append(book('博客來', links[i], names[i], 0, discount_price, author, publisher, publish_date, booktype, imgs[i]))
    
    return item_list
