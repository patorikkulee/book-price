import requests
import codecs
import ast
from bs4 import BeautifulSoup as bs
from book_info import book

domain = 'https://www.angle.com.tw/'

def str_encode(s:str):
    s = s.encode('big5').__str__()
    s = s.lstrip("b'").rstrip("'")
    s = s.replace('\\x', '%')

    return s

def preprocess_string(s:str):
    s = s.replace(' ', '')
    s = s.replace('\r', '')
    s = s.replace('\n', '')
    s = s.replace('\xa0', '')
    return s

def search_angle(keyword:str):
        
    keyword = str_encode(keyword)
    url = f'http://www.angle.com.tw/search.asp?keyword={keyword}&col=1'
    page = requests.get(url)
    page.encoding = 'big5'

    soup = bs(page.text, "html.parser")
    items = soup.find_all('tr')[12:-8]

    item_list = []
    for each in items:
        info = each.find_all('td')
        serialnum = preprocess_string(info[0].text)
        name = preprocess_string(info[1].text)
        link = domain + info[1].find('a')['href']
        author = preprocess_string(info[2].text)
        publisher = preprocess_string(info[3].text)
        price = preprocess_string(info[4].text)
        discount_price = preprocess_string(info[5].text)
        
        item_list.append(book('元照', link, name, price, discount_price, author, publisher, serialnum=serialnum))

    return item_list
