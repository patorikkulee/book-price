class book:
    def __init__(self, site, link, name, price, discount_price, author='', publisher='', publish_date='', type='', image='', serialnum=''):
        self.site = site
        self.link = link
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.type = type
        self.image = image
        self.serialnum = serialnum
    
    @property
    def lowest_price(self):
        if self.price==0:
            return self.discount_price
        elif self.discount_price==0:
            return self.price
        else:
            return min(self.price, self.discount_price)


    def __str__(self):
        info = f"""{'--'*30}
網站: {self.site}
連結: {self.link}
書名: {self.name}
原價: {self.price if self.price != 0 else ''}
特價: {self.discount_price if self.discount_price != 0 else '無'}
作者: {self.author}
出版社: {self.publisher}
出版日期: {self.publish_date}
類別: {self.type}
圖示: {self.image}"""
        return info

    def get_html(self):
        td = f'''
        <img src="{self.image}" width="135" height="200"><br>
        <a href="{self.link}">{self.name}</a><br>
        <ul>
        <li>網站: {self.site}</li>
        <li>原價: {self.price if self.price != 0 else '無'}</li>
        <li>特價:  {self.discount_price if self.discount_price != 0 else '無'}</li>
        <li>作者: {self.author}</li>
        <li>出版社: {self.publisher}</li>
        <li>出版日期: {self.publish_date}</li>
        <li>類別: {self.type}</li>
        </ul>
        -------------------------------<br>
'''
        return td


def sort_price(bookslist, ascending=True):
    if ascending==False:
        return sorted(bookslist, key=lambda x: x.lowest_price, reverse=True)
    return sorted(bookslist, key=lambda x: x.lowest_price)
