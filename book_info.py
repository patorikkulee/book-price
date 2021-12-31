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

    # def __str__(self):
    #     return f"{self.site} : {self.name}"

    def __str__(self):
        info = f"""{'--'*30}
網站: {self.site}
連結: {self.link}
書名: {self.name}
原價: {self.price if self.price != 0 else '無'}
特價: {self.discount_price if self.discount_price != 0 else '無'}
作者: {self.author}
出版社: {self.publisher}
出版日期: {self.publish_date}
類別: {self.type}
圖示: {self.image}"""
        return info

    def get_html(self):
        td = f'''    <tr>
        <td align="left">
            <img src="{self.image}" width="200" height="300">
        </td>
        <td align="right", valign="top">
            網站: {self.site}<br>
            <a href="{self.link}">{self.name}</a><br>
            原價: {self.price if self.price != 0 else '無'}<br>
            特價:  {self.discount_price if self.discount_price != 0 else '無'}<br>
            作者: {self.author}<br>
            出版社: {self.publisher}<br>
            出版日期: {self.publish_date}<br>
            類別: {self.type}<br>
            ----------------------------<br>
        </td>
    </tr>
'''
        return td

'''
class booklist:
    def __init__(self, books):
        self.books = books
    
    def sort_price(self, ascending=True):
        if ascending==False:
            return sorted(self.books, key=lambda x: x.lowest_price, reverse=True)
        return sorted(self.books, key=lambda x: x.lowest_price)
'''
def sort_price(bookslist, ascending=True):
    if ascending==False:
        return sorted(bookslist, key=lambda x: x.lowest_price, reverse=True)
    return sorted(bookslist, key=lambda x: x.lowest_price)
