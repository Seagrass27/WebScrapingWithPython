from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=
                          'd:\\Anaconda\\Scripts\\chromedriver.exe',
                          chrome_options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()

#还用BeautifulSoup解析网页内容
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path=
                          'd:\\Anaconda\\Scripts\\chromedriver.exe',
                          chrome_options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
pageSource = driver.page_source #返回网页源代码字符串
bsObj = BeautifulSoup(pageSource)
print(bsObj.find(id = 'content').get_text())
driver.close()

#让Selenium不断检查某个元素是否存在，确定页面完全加载，如果加载成功就执行后面程序
#WebDriverWait和EC组合构成隐式等待(DOM某个状态发生后再继续运行)
#EC定义触发DOM的状态
#BY表示定位器，在这里用来指定等待的目标元素
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('d:\\Anaconda\\Scripts\\chromedriver.exe',
                          chrome_options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')

try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'loadedButton')))
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()

#处理客户端重定向
#监视DOM中的一个元素，元素不在DOM中时说明网页已经跳转
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 200:
            print('Timing out after 10 seconds and returning')
            return
        time.sleep(.1)
        try:
            elem == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('d:\\Anaconda\\Scripts\\chromedriver.exe',
                          chrome_options=chrome_options)

driver.get('http://pythonscraping.com/pages/javascript/redirectDemo1.html')
waitForLoad(driver)
print(driver.page_source)
driver.close()