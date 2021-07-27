# Corinne Bradford
# CS361 Summer 2021

from bs4 import BeautifulSoup
import requests
import re


def img_scraper(keyword):
    keyword = keyword.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + keyword
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    for image in soup.findAll("img"):
        # src = image.get('src')
        if re.search('wikipedia/.*/thumb/', image.get('src')) and not re.search('.svg', image.get('src')):
            return image.get('src')
    return "could not find image"
