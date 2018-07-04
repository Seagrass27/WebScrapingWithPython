from urllib.request import urlopen
from bs4 import BeautifulSoup

# =============================================================================
# 找出属性class的值为green的span标签
# =============================================================================
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html)

# .find_all returns a list of Tag objects
namelist = bsObj.find_all('span',{'class':'green'})
for name in namelist: 
    print(name.get_text()) # get_text()用来获取tag的内容

# =============================================================================
# 找出属性id值为giftList的table标签的子标签
# =============================================================================
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html)

for child in bsObj.find('table',{'id':'giftList'}).children:
    print(child)
# 区分descendant和child的区别
for descendant in bsObj.find('table',{'id':'giftList'}).descendants:
    print(descendant)
    
# 处理兄弟标签
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)
    
# 父标签处理
print(bsObj.find('img',{'src':'../img/gifts/img1.jpg'
                        }).parent.previous_sibling.get_text())
# =============================================================================
# 配合正则表达式使用BeautifulSoup
# =============================================================================
import re
images = bsObj.find_all('img',{'src':re.compile('\.\.\/img/gifts\/img.*\.jpg')})
for image in images:
    print(image['src']) 

# =============================================================================
# 获取tag的属性(images[0]是一个tag)
# =============================================================================
images[0].attrs # 返回一个包含这个tag所有属性及其属性值的字典
images[0].attrs['src'] # 通过字典获取src属性的值
images[0]['src'] # 直接获取这个tag的src属性的值

# =============================================================================
# Lamda表达式
# =============================================================================
# 找出有两个属性的标签
for i in bsObj.find_all(lambda tag: len(tag.attrs) ==2):
    print(i,'\n\n')