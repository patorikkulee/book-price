class book:
    def __init__(self, name, price, discount_price, author='', publisher='', publish_date='', image=''):
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.image = image

bk1 = book('民法', 300, 200, '帥李', '台大出版社', '2021-12-22', '123456789')
print(bk1.name)