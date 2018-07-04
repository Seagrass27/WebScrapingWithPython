# 维基百科六度分割
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

# 存储贝肯数不超过6的页面
conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = '123',
                       db = 'mysql', charset = 'utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def insertPageIfNotExist(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0] # 取出这个page的id

def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s',
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES(%s, %s)',
                    (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExist(pageUrl)
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find_all('a',href = re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExist(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel + 1)
getLinks('/wiki/Kevin_Bacon',0)     

cur.close()
conn.close()

# 利用这两个数据表，实现一个广度优先搜索算法
conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = '123',
                       db = 'mysql', charset = 'utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

class SolutionFound(RuntimeError): #继承RuntimeError类
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s', (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))
    return {}

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree: #该节点没有连接则跳过该节点
            return {}
    if targetPageId in linkTree.keys():
        print('Target ' + str(targetPageId) + 'Found!')
        raise SolutionFound('Page: ' + str(currentPageId))
    
    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, 
                    branchValue, depth - 1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound('Page: ' + str(currentPageId))
    return linkTree

try:
    searchDepth(2, 1, {}, 4)
    print('No solution found.')
except SolutionFound as e:
    print(e.message)
