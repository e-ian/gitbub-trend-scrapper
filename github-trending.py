import requests
from bs4 import BeautifulSoup

# Collect the github page
page = requests.get('https://github.com/trending')

#create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get repo list
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

# find all instances of that class (return 25 as shown on github main page)
repo_list = repo.find_all(class_="Box-row")

print(len(repo_list))

for repo in repo_list:
    # find first <h1> tag and get the text. split text with '/' to get an array with developer name and repo name
    full_repo_name = repo.find('h1').text.split('/')
    # extract the developer name at index 0
    developer = full_repo_name[0].strip()
    # extract the repo name at index 1
    repo_name = full_repo_name[1].strip()
    # first occurence of class octicon octicon-star and get the text from the parent(number of stars)
    stars = repo.find(class_="octicon octicon-star").parent.text.strip()
    
    print('developer', developer)
    print('name', repo_name)
    print('stars', stars)
