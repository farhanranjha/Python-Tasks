import requests
from bs4 import BeautifulSoup


def getPage(paramURL, paramRequired):
    r = requests.get(paramURL)
    soup = BeautifulSoup(r.content, 'html.parser')

    for item in soup.findAll("div"):
        if item.get('class') == paramRequired:
            print(item.text)
            print(str(item.findChildren(
                "a", recursive=False)).split('"')[1][7:])
            print('\n')


URL = "https://www.google.com/search?q="
required = ['egMi0', 'kCrYT']

print("Enter the keyword: ")
keyword = input()

print("Number of results: ")
number = int(input())

myUrl = URL + keyword + "&start=" + str(number)
getPage(myUrl, required)
