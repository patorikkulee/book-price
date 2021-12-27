import requests
from bs4 import BeautifulSoup as bs 
from book_info import book

keyword = "民法"
url = f'https://sharing.com.tw/book_list_s.php?book_whit=0&book_data={keyword}&MM_update=form1'
page = requests.get(url)
soup = bs(page.text, "html.parser")


items = soup.find_all("td", {"align": "left"})
imgs = soup.find_all("td", {"align": "center"})

item_list = []
for i, img in list(zip(items, imgs)):
    name = i.find("td", {"class": "publishername"}).text
    publisher = i.find("td", {"class": "publisher"}).text
    image = img.find('img')['src']
    try:
        author = i.find("td", {"class": "publisher_au"}).text
    except AttributeError:
        author = ""

    for j in i.find_all("td", {"class": "publishertype"}):
        info = j.text
        
        if '出版日' in info:
            publish_date = info.split('：')[-1]
        elif '定價' in info:
            price = info.split('：')[-1]
        elif '特價' in info:
            discount_price = info.split('：')[-1]
        else:
            publish_date = price = discount_price = ''

    item_list.append(book(name, price, discount_price, author, publisher, publish_date, image))

    # print(i.find_all("td", {"class": "publishertype"}).text)
    print('----------------------------------------------')

print(item_list)

# print(items[-1], len(items))
# booknames = soup.find_all("td", {"class": "publishername"})
# publishers = soup.find_all("td", {"class": "publisher"})
# imgs = soup.find_all("img")
# imgs = [x['src'] for x in imgs if 'pictures' in x['src']]
# dates_prices = publishers = soup.find_all("td", {"class": "publishertype"})
# dates = prices = []
# for i in dates_prices:
#     dateNprice = i.split(' ')
#     dates.append(dateNprice[0])
#     prices.append(dateNprice[1])


# for i in imgs:
#     print(i.find('img')['src'])

# print(len(imgs))

# print(len(imgs))
    # print(i['src'])

# for b, p, d in list(zip(booknames, publishers, dates)):
#     print(b.text,'\n',p.text, '\n', d.text)
