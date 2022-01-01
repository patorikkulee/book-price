from tkinter import *
from book_info import *
from angle import search_angle
from books import search_books
from sharing import search_sharing
from tkhtmlview import HTMLLabel


window = Tk() # open new window
window.title('法律書籍比價搜尋') # set title
window.iconbitmap('law_icon.ico') # set icon
window.geometry('500x600') # set window size

html_head = '''<!DOCTYPE html>
<html lang="zh-tw">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
'''
html_tail = """    </body>
</html>

"""
html_final = '<head></head>'
itemlist = []

# set key bindings
def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

window.bind_all("<Key>", _onKeyRelease, "+")


# search 3 sites and return list of books
def search_all(keyword:str)->list:
    itemlist = search_books(keyword)
    itemlist += search_angle(keyword)
    itemlist += search_sharing(keyword)
    
    return itemlist


# clear all text boxes
def clear():
    entry.delete(1.0, END)
    html_label.set_html(html='<head></head>')


# search books
def search():
    keyword = entry.get(1.0, END).rstrip('\n')
    global itemlist
    itemlist = search_all(keyword)
    itemlist = sort_price(itemlist)
    
    list_html = ''.join([i.get_html() for i in itemlist])
    html_final = html_head + list_html + html_tail
    html_label.set_html(html=html_final)


def sort_descending():
    global itemlist
    itemlist = itemlist[::-1]
    list_html = ''.join([i.get_html() for i in itemlist])
    html_final = html_head + list_html + html_tail
    html_label.set_html(html=html_final)


# label for entry
entry_label = Label(window, text="輸入書名")
entry_label.pack(pady=10)

# textbox of entry
entry = Text(window, height=2, borderwidth=2)
entry.pack(pady=10)

# initialize button object
button_frame = Frame(window)
button_frame.pack()

# create search button
search_button = Button(button_frame, text='搜尋', command=search)
search_button.grid(row=0, column=1)

# create sort price descending button
clear_button = Button(button_frame, text='價格由高到低', command=sort_descending)
clear_button.grid(row=0, column=2)

# create clear button
clear_button = Button(button_frame, text='清除', command=clear)
clear_button.grid(row=0, column=3)

# label for search result
output_label = Label(window, text="搜尋結果")
output_label.pack(pady=10)

# html
html_label = HTMLLabel(window, html=html_final)
html_label.pack(fill='both', expand=True)
html_label.fit_height()

window.mainloop()
