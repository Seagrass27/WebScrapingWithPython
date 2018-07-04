from urllib.request import urlopen
from bs4 import BeautifulSoup

#textPage是HTTPResponse对象，textPage.read()返回的是bytes对象
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/'\
                   'chapter1-ru.txt')
print(textPage.read()) # Python默认把它读成ASCII编码格式

textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/'\
                   'chapter1-ru.txt')
print(str(textPage.read(), 'utf-8')) # 正确显示斯拉夫文字
# =============================================================================
# 文本编码
# =============================================================================
#----------------------------------------------------------------------
u = '中文' #指定字符串类型对象u
my_str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes对象
u1 = my_str.decode('gb2312') #以gb2312编码对bytes对象进行解码，获得字符串对象u1
u2 = my_str.decode('utf-8') #如果以utf-8的编码对bytes对象进行解码，
                            #将无法还原原来的字符串内容
#----------------------------------------------------------------------
html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html)
content = bsObj.find('div',{'id':'mw-content-text'}).get_text() #得到字符串对象
content_bytes = bytes(content,'utf-8') #相当于用encode函数，得到bytes对象
content_byte1 = content.encode('utf-8')
print(content_bytes == content_byte1)
content_1 = content_bytes.decode('utf-8')
print(content == content_1)
# =============================================================================
# csv文件
# =============================================================================
from urllib.request import urlopen
from io import StringIO
import csv

string_data = urlopen('http://pythonscraping.com/files/'\
                          'MontyPythonAlbums.csv').read().decode('ascii')
file_data = StringIO(string_data) #将字符串封装成StringIO对象，
                                  #从而让python把它当成文件来处理
                                  
csvReader = csv.reader(file_data) #返回一个可迭代对象，由列表构成
for row in csvReader:
    print(row)

file_data = StringIO(string_data)
dictReader = csv.DictReader(file_data) #返回一个可迭代对象，由字典构成
print(dictReader.fieldnames)
for row in dictReader:
    print(row)
# =============================================================================
# PDF文件
# =============================================================================
#略
# =============================================================================
# .docx格式文件
# =============================================================================
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

word_bytes = urlopen('http://pythonscraping.com/pages/AWordDocument.docx')\
                     .read()
word_file = BytesIO(word_bytes) #将bytes类型对象封装成BytesIO类型对象
document = ZipFile(word_file) #解压缩
xml_content = document.read('word/document.xml') #得到bytes类型对象
print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'))
textStrings = wordObj.find_all('w:t') #找不到这个标签!

for textElem in textStrings:
    print(textElem.text)


