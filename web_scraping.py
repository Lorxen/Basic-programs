# Web scrapper to get info from a web page

import requests
from bs4 import BeautifulSoup

url = 'https://www.ziperto.com/'
r = requests.get(url)

# Get the web info
soup = BeautifulSoup(r.content, 'html.parser')

# Sort the information you want
title = soup.find_all('h2', {'class':'post-title'})

# Print the list of the information we are looking for
for t in title:
    print(t.getText())