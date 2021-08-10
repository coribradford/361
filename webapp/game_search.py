# Corinne Bradford
# CS361 Summer 2021

# from tkinter import *

# root = Tk()

# def click_search():
#     game_name_label_widget = Label(root, text=entry_widget.get())
#     entry_widget.delete(0, END)
#     game_name_label_widget.grid(row=2, column=0)

# root.title("Game Search Engine")
# root.iconbitmap('games.ico')
# instructions_label_widget = Label(root, text="Enter a game to search")
# instructions_label_widget.grid(row=1, column=0)

# entry_widget = Entry(root, width=50)
# entry_widget.grid(row=0, column=0)


# button_widget = Button(root, text="Search", command=click_search)
# button_widget.grid(row=0, column=1)

# root.mainloop()

from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)