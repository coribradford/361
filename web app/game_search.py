# Corinne Bradford
# CS361 Summer 2021


import tkinter as tk
import requests
import re
import time

root = tk.Tk()
w = tk.Message(root, text="Welcome")
m = tk.Button(root, text="Hello")
w.pack()
m.pack()
root.mainloop()

# class Main(tk.Frame):
#     def __init__(self, root):
#         super().__init__(root)
#         self.grid()
#         self.language = 'en'
#         self.root = root

#     def set_language(self, language):
#         self.language = language

#     def search_text(self, event):
#         keyword = self.search_set.search.get()
#         if keyword == "":
#             root.focus()
#             return
#         self.search_set.search.delete(0, tk.END)

#         if keyword != self.search_set.get_tooltip():
#             self.search_set.search.insert(0, "Enter game to search")

#         root.focus()

# class Homepage(tk.Frame):

#     def __init__(self, root):
#         tk.Frame.__init__(self, root)
#         self['borderwidth'] = 1
#         self["relief"] = 'groove'

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Game Search Engine") 
#     root.resizable(True, True)
#     root.geometry("680x650")
#     app = Main(root)
#     root.mainloop()