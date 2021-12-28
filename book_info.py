class book:
    def __init__(self, name, price, discount_price, author='', publisher='', publish_date='', image=''):
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.image = image

    def __str__(self):
        info = f"""
作者: {self.author}
原價: {self.price}
特價: {self.discount_price}
出版商: {self.publisher}
出版日期: {self.publish_date}"""
        return info
