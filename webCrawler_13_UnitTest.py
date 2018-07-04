# =============================================================================
# 用爬虫测试网站
# =============================================================================

#单元测试
import unittest

class TestAddition(unittest.TestCase):
    def setUp(self):
        print('Setting up the test')
    
    def tearDown(self):
        print('Tearing down the test')
        
    def test_twoPlustwo(self):
        total = 2 + 2
        self.assertEqual(4, total)
        
    def test_threePlusthree(self):
        total = 3 + 3
        self.assertEqual(6, total)
        
if __name__ == '__main__':
    unittest.main()

#测试维基百科
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        global bsObj
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        bsObj = BeautifulSoup(urlopen(url))
    
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle)
        
    def test_contentExists(self):
        global bsObj
        content = bsObj.find('div',{'id':'mw-content-text'})
        self.assertIsNotNone(content)
        
if __name__ == '__main__':
    unittest.main()

#用Selenium与网站交互
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('d:\\Anaconda\\scripts\\chromedriver.exe',
                          options = chrome_options)
driver.get('http://pythonscraping.com/pages/files/form.html')


firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

###方法一##：
firstnameField.send_keys('Tyrell')
lastnameField.send_keys('Sun')
submitButton.click()
###########

###方法二##:
actions = (ActionChains(driver).click(firstnameField).send_keys('Tyrell')
                               .click(lastnameField).send_keys('Sun')
                               .send_keys(Keys.RETURN))
actions.perform()
###########

print(driver.find_element_by_tag_name('body').text)
driver.close()

#鼠标拖放动作
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('d:\\Anaconda\\scripts\\chromedriver.exe',
                          options = chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')

print(driver.find_element_by_id('message').text)

element = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('div2')
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()

print(driver.find_element_by_id('message').text)

#截屏
driver.get_screenshot_as_file('c:\\users\\asus\\desktop\\screenshot.png')
driver.close()
