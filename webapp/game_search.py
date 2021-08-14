# Corinne Bradford
# CS361 Summer 2021

from flask import *
import wikipedia
from bs4 import BeautifulSoup
import requests
import re
import urllib
import datetime
import json

app = Flask(__name__)


def wiki_summary(keyword):
    try:
        summary = wikipedia.summary(keyword, auto_suggest=False, sentences=6)
        return summary
    except wikipedia.exceptions.PageError or wikipedia.exceptions.DisambiguationError:
        return -1


def wiki_title(keyword):
    try:
        url = 'https://en.wikipedia.org/wiki/' + keyword
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        words =  soup.findAll("h1")
        title = words[0].text
        return title, url
    except wikipedia.exceptions.PageError or wikipedia.exceptions.DisambiguationError:
        return -1


def featured_wiki_title():
    today = datetime.datetime.now()
    date = today.strftime('%Y/%m/%d')
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/featured/' + date
    page = urllib.request.urlopen(url)
    data = json.loads(page.read())
    return data['tfa']['title']


def random_keyword():
    return str(wikipedia.random(pages=1))


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
        url = "https://www.youtube.com/results?search_query=" + keyword
        html = urllib.request.urlopen(url)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        return video_ids[0]
    except urllib.error.HTTPError:
        return


def get_info(keyword):
    summary = wiki_summary(keyword)
    title, url = wiki_title(keyword)
    image = img_scraper(title)
    video_id = video_id_lookup(title)
    payload = {"videoid": video_id}
    response = requests.get("http://flip1.engr.oregonstate.edu:65334/embedlink", params=payload)
    link = response.text
    google_keyword = title.replace(" ", "+")
    google_url = "https://www.google.com/search?q=" + google_keyword
    return summary, title, url, image, link, google_url


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        if request.form.get("featured") == "Featured Article":
            return redirect(url_for(featured))
        if request.form.get("random") == "Random Article":
            return redirect(url_for(featured))
        else:
            search_info = request.form["search_input"]
            summary, title, wiki_url, image, link, google_url = get_info(search_info)
            return render_template("search.html", title=title, content=summary, wiki=wiki_url, picture=image, embed=link, google=google_url)
    else:
        return render_template("index.html")


@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


@app.route("/featured", methods=["GET", "POST"]) 
def featured():
    search_info = featured_wiki_title()
    summary, title, wiki_url, image, link, google_url = get_info(search_info)
    return render_template("featured.html", title=title, content=summary, wiki=wiki_url, picture=image, embed=link, google=google_url)


@app.route("/random", methods=["GET", "POST"]) 
def random():
    search_info = random_keyword()
    summary, title, wiki_url, image, link, google_url = get_info(search_info)
    return render_template("random.html", title=title, content=summary, wiki=wiki_url, picture=image, embed=link, google=google_url)


if __name__ == "__main__":
    app.run(debug=True)
