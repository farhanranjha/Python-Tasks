import requests
from bs4 import BeautifulSoup
from distutils.log import debug
from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'My First API!'


@app.route('/google/<string:keyword>')
def getPage(keyword):
    paramRequired = ['egMi0', 'kCrYT']
    URL = "https://www.google.com/search?q="+keyword
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    outFile = open("/Users/apple/Desktop/text.txt", "a");
    

    for item in soup.findAll("div"):
        if item.get('class') == paramRequired:
            # print(item.text)
            # print(str(item.findChildren(
            #     "a", recursive=False)).split('"')[1][7:])
            # print('\n')
            outFile.write(item.text + "\n\n" + (str(item.findChildren("a", recursive=False)).split('"')[1][7:]) + "\n\n\n\n")
    return send_file("/Users/apple/Desktop/text.txt")


app.run(debug=True)
