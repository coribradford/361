# Corinne Bradford
# CS361 Summer 2021

import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpim

page = requests.get('https://store.steampowered.com/app/238960/Path_of_Exile/?snr=1_4_4__118')
# test page
soup = BeautifulSoup(page.content, 'html.parser')
images = soup.findAll('img')


for item in images:
    print(item['src'])

# img = mpim.imread(images[0])
# imgplot = plt.imshow(img)
# plt.show()
# currently grabs and prints all image urls - make this useful somehow