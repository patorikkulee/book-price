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

    def __str__(self):
        return f"{self.site} : {self.name}"

    def __repr__(self):
        info = f"""{'+-'*30}
網站: {self.site}
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

    def get_html(self):
        td = f'''    <tr>
        <td align="left">
            <img src="{self.image}" width="100" height="150">
        </td>
        <td align="right">
            網站: {self.site}<br>
            <a href="{self.link}">{self.name}</a><br>
            原價: {self.price}<br>
            特價:  {self.discount_price}<br>
            作者: {self.author}<br>
            出版社: {self.publisher}<br>
            出版日期: {self.publish_date}<br>
            類別: {self.type}<br>
        </td>
    </tr>
'''
        return td
