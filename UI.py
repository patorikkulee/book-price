from tkinter import *
from book_info import *
from angle import search_angle
from books import search_books
from sharing import search_sharing
from tkhtmlview import HTMLLabel


window = Tk() # open new window
window.title('法律書籍比價搜尋') # set title
window.iconbitmap('law_icon.ico') # set icon
window.geometry('800x600') # set window size

html_head = """<!DOCTYPE html>
<html lang="zh-tw">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <table>
"""

html_tail = """        </table>
    </body>
</html>

"""
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


def search_all(keyword:str)->list:
    itemlist = search_books(keyword)
    itemlist += search_angle(keyword)
    itemlist += search_sharing(keyword)
    
    return itemlist


# clear all text boxes
def clear():
    entry.delete(1.0, END)
    html_label = HTMLLabel(window, html='<head></head>')
    html_label.pack(fill='both', expand=True)
    html_label.fit_height()
    # HTMLLabel.delete(0, END)


# search books
def search():
    keyword = entry.get(1.0, END).rstrip('\n')
    itemlist = search_all(keyword)
    itemlist = sort_price(itemlist)
    # listbox.insert("end", *itemlist)
    list_html = ''.join([i.get_html() for i in itemlist])
    html_label = HTMLLabel(window, html=html_head + list_html + html_tail)
    html_label.pack(fill='both', expand=True)
    html_label.fit_height()


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

# create clear button
clear_button = Button(button_frame, text='清除', command=clear)
clear_button.grid(row=0, column=2)

# label for search result
output_label = Label(window, text="搜尋結果")
output_label.pack(pady=10)


window.mainloop()
