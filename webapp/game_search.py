# Corinne Bradford
# CS361 Summer 2021

from tkinter import *

root = Tk()

def click_search():
    game_name_label_widget = Label(root, text=entry_widget.get())
    game_name_label_widget.pack()


title_label_widget = Label(root, text="Game Search Engine")
instructions_label_widget = Label(root, text="Enter a game to search")
title_label_widget.pack()
instructions_label_widget.pack()

entry_widget = Entry(root, width=50)
entry_widget.pack()


button_widget = Button(root, text="Search", command=click_search)
button_widget.pack()

root.mainloop()