import requests
from bs4 import BeautifulSoup

# Collect the github page
page = requests.get('https://github.com/trending')

#create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get repo list
# repo = soup.find(class_="Box")

# find all instances of that class (return 25 as shown on github main page)
repo_list = soup.find_all(class_="Box-row")

print(len(repo_list))
