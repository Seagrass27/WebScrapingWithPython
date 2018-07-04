from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
url = "http://www.pythonscraping.com/pages/page1.html"

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body
    except AttributeError as e:
        return None
    return title

title = getTitle(url)
if title == None:
    print('Title could not be found!')
else:
    print(title)
