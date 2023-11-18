import requests
from bs4 import BeautifulSoup
import urllib

base_url = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

# get all image urls
urls = []
for link in soup.find_all('a'):
    if link.get('href').endswith('416x250.jpg'):
        urls.append(link.get('href'))

# get a day's worth of hourly images
urls = urls[::12][:24]
# download images
for url in urls:
    im = requests.get(base_url + url).content
    f = open(url,'wb')
    f.write(im)
    f.close()