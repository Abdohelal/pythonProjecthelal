from bs4 import BeautifulSoup
import requests
import itertools
list1 = []
list2 = []
URL = 'https://www.amazon.eg/s?i=electronics&bbn=21832907031&rh=n%3A21832907031%2Cp_n_feature_twenty-three_browse-bin%3A27388032031%2Cp_89%3AApple&dc&language=en&ds=v1%3A1BFxnXdvau%2FnUJxtStKmmnJXcRhFusCBtXs5%2F%2Bb%2BQCE&qid=1671299329&rnid=22541269031&ref=sr_nr_p_89_1'
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
src = webpage.content
soup = BeautifulSoup(src, "lxml")
#print(soup)
lapinfo = soup.find_all("h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
priceinfo = soup.find_all("span", {"class": "a-price-whole"})
for i in range(len(lapinfo)):
    list1.append(lapinfo[i].text)

for j in range(len(priceinfo)):
    list2.append(priceinfo[j].text)

for (i,j) in itertools.zip_longest(list1,list2):
    print(i,j)
from bs4 import BeautifulSoup
import requests
import itertools
list1 = []
list2 = []
URL = 'https://www.amazon.eg/s?i=electronics&bbn=21832907031&rh=n%3A21832907031%2Cp_n_feature_twenty-three_browse-bin%3A27388032031%2Cp_89%3AApple&dc&language=en&ds=v1%3A1BFxnXdvau%2FnUJxtStKmmnJXcRhFusCBtXs5%2F%2Bb%2BQCE&qid=1671299329&rnid=22541269031&ref=sr_nr_p_89_1'
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 Safari / 537.36',
    'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
src = webpage.content
soup = BeautifulSoup(src, "lxml")
#print(soup)
lapinfo = soup.find_all("h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
priceinfo = soup.find_all("span", {"class": "a-price-whole"})
for i in range(len(lapinfo)):
    list1.append(lapinfo[i].text)

for j in range(len(priceinfo)):
    list2.append(priceinfo[j].text)

for (i,j) in itertools.zip_longest(list1,list2):
    print(i,j)

