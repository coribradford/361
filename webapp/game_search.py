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
import wikipedia
from bs4 import BeautifulSoup
import requests
import re
import urllib

app = Flask(__name__)

def wiki_scraper(keyword):
    try:
        length = len(keyword)
        summary = wikipedia.summary(keyword, auto_suggest=False, sentences=6)
        title = summary[:length]
        returns = [title, summary]
        return returns
    except wikipedia.exceptions.PageError:
        return "Could not find entry."
    except wikipedia.exceptions.DisambiguationError as e:
        return "Too many possibilities, please be more specific."

def img_scraper(keyword):
    keyword = keyword.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + keyword
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for image in soup.findAll("img"):
        src = image.get('src')
        if re.search('wikipedia/.*/thumb/', src) and not re.search('.svg', src):
            return src
    return -1

def video_id_lookup(keyword):
    try:
        keyword = keyword.replace(" ", "+")
        print(keyword)
        keyword = keyword + "+trailer"
        url = "https://www.youtube.com/results?search_query=" + keyword
        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        return video_ids[0]
    except urllib.error.HTTPError:
        return "dQw4w9WgXcQ"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_info = request.form["search_input"]
        output = wiki_scraper(search_info)
        image = img_scraper(search_info)
        id = video_id_lookup(search_info)
        payload = {"videoid": id}
        response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
        link = response.text
        return render_template("search.html", game_title=output[0], content=output[1], picture=image, embed=link)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)