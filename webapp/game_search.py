# Corinne Bradford
# CS361 Summer 2021

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
        title = summary[:(length+1)]
        returns = [title, summary]
        return returns
    except wikipedia.exceptions.PageError:
        return [-1, -1]
    except wikipedia.exceptions.DisambiguationError as e:
        return [-1, -1]

def img_scraper(keyword):
    keyword = keyword.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + keyword
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for image in soup.findAll("img"):
        src = image.get('src')
        if re.search('wikipedia/.*/thumb/', src) and not re.search('.svg', src):
            return src
    return

def video_id_lookup(keyword):
    try:
        keyword = keyword.replace(" ", "+") + "+game+trailer"
        url = "https://www.youtube.com/results?search_query=" + keyword
        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        return video_ids[0]
    except urllib.error.HTTPError:
        return


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_info = request.form["search_input"]
        output = wiki_scraper(search_info)
        if output is not None:
            title = output[0]
            summary = output[1]
        else:
            title = "hold"
            summary = "hold"
        image = img_scraper(search_info)
        id = video_id_lookup(search_info)
        payload = {"videoid": id}
        response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
        link = response.text
        return render_template("search.html", game_title=title, content=summary, picture=image, embed=link)
    else:
        return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
    # using debug = True for dev purposes only