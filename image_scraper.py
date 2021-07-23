# Corinne Bradford
# CS361 Summer 2021

from bs4 import BeautifulSoup
import requests
import re

def img_scraper(keyword):
    keyword = keyword.replace(" ", "_")
    url = 'https://wikipedia.org/wiki/' + keyword
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.findAll('img')
    for item in images:
        # img = mpim.imread(item['src'])
        # imgplot = plt.imshow(img)
        # plt.show()
        print(item['src'])


def main():
    keyword = "Flags"
    img_scraper(keyword)

main()

if __name__ == '__main__':
    main()
