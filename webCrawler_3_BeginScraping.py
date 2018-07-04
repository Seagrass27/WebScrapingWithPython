from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)

for link in bsObj.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'],'\n') # 打印出一个wiki页面中所有链接

# 只保留词条链接
# 词条链接特点：
# 1. 都在id是bodyContent的div标签里
# 2. URL链接都不包含冒号
# 3. URL链接都以/wiki/开头
import re

for link in bsObj.find('div',{'id':'bodyContent'}).find_all('a',
                      href = re.compile('^(/wiki/)((?!:).)*$')):
    print(link.attrs['href'])

# =============================================================================
# 主函数以某个起始词条作为参数调用getLinks，再从返回的URL列表中随机选一个词条链接，
# 再调用getLinks，直到我们主动停止或新的页面没有词条链接，程序中止
# =============================================================================
import datetime
import random

random.seed(datetime.datetime.now())

# 返回带有词条链接的a标签列表
def getLinks(articleUrl):
    url = 'http://en.wikipedia.org' + articleUrl
    html = urlopen(url)
    bsObj = BeautifulSoup(html,'html.parser')
    return bsObj.find('div',{'id':'bodyContent'}).find_all('a',
                     href = re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

# =============================================================================
# 采集整个网站,收集整个网站数据
# =============================================================================
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print('标题:',bsObj.h1.get_text())
        print('第一段文字:',bsObj.find(id = 'mw-content-text').find_all('p')[0])
        print('编辑链接:',
              bsObj.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面缺少一些属性！')
    
    for link in bsObj.find_all('a',href = re.compile('^(/wiki/)')):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print('-------------------------------\n' + newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks('')