from tkinter import *
from angle import search_angle
from books import search_books
from sharing import search_sharing

def populateListbox(items):
    listbox.insert("end", *items)

def search_all(keyword:str)->list:
    itemlist = search_angle(keyword)
    itemlist += search_books(keyword)
    itemlist += search_sharing(keyword)
    
    return itemlist

window = Tk() # open new window
window.title('法律書籍比價搜尋') # set title
window.geometry('800x600') # set window size

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

# clear all text boxes
def clear():
    entry.delete(1.0, END)

def search():
    keyword = entry.get(1.0, END).rstrip('\n')
    itemlist = search_all(keyword)
    listbox.insert("end", *itemlist)

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

listbox = Listbox(window)
listbox.pack()

window.mainloop()
