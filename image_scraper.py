# Corinne Bradford
# CS361 Summer 2021

import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpim


def img_scraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.findAll('img')

    for item in images:
        img = mpim.imread(item['src'])
        imgplot = plt.imshow(img)
        plt.show()


def main():
    url = 'https://store.steampowered.com/app/238960/Path_of_Exile/?snr=1_4_4__118'
    img_scraper(url)

if __name__ == '__main__':
    main()