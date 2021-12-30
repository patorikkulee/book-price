# from tkinterweb import HtmlFrame
from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
# frame = HtmlFrame(root)
# frame.load_html("test.html")
# frame.pack(fill='both', expand=True)
label = HTMLLabel(root, html='<img src="https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/090/28/0010902826.jpg" width="100" height="150">')
label.pack(fill='both', expand=True)
root.mainloop()
