class book:
    def __init__(self, link, name, price, discount_price, author='', publisher='', publish_date='', type='', image=''):
        self.link = link
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.type = type
        self.image = image

    def __str__(self):
        info = f"""{'+-'*30}
連結: {self.link}
書名: {self.name}
原價: {self.price}
特價: {self.discount_price}
作者: {self.author}
出版社: {self.publisher}
出版日期: {self.publish_date}
類別: {self.type}
圖示: {self.image}"""
        return info
