import requests
from bs4 import BeautifulSoup

# Collect the github page
page = requests.get('https://github.com/trending')
print(page)

#create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)
