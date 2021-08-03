# Corinne Bradford
# CS361 Summer 2021

from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
import requests
import re

app = Flask(__name__)

def img_scraper(keyword):
    keyword = keyword.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + keyword
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for image in soup.findAll("img"):
        src = image.get('src')
        if re.search('wikipedia/.*/thumb/', src) and not re.search('.svg', src):
            return src
    return "could not find image"

@app.route('/')
def hello():
    """Return http greeting"""
    return "Welcome to Cori's Image scraper service! Search for an image with '/get_img/keyword'"

@app.route('/get_img/')
def doc():
    """instructions"""
    return "search for an image with '/get_img/keyword'"

@app.route('/get_img/<keyword>')
def get_img(keyword):
    """image scraper"""
    img = img_scraper(keyword)
    return jsonify(img)
