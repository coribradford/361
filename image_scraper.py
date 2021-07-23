# Corinne Bradford
# CS361 Summer 2021

import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://store.steampowered.com/app/238960/Path_of_Exile/?snr=1_4_4__118')
# test page
soup = BeautifulSoup(page.content, 'html.parser')
images = soup.findAll('img')


for item in soup.findAll('img'):
    print(item['src'])

# currently grabs and prints all image urls - make this useful somehow