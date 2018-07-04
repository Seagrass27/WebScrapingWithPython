# =============================================================================
# 避免采集陷阱
# =============================================================================

# 修改请求头
import requests
from bs4 import BeautifulSoup

session  = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
                         'AppleWebKit 537.36*(KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
                    'q=0.9,image/webp,*;q=0.8'}
url = ('https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser'
      '-sending')
req = session.get(url, headers = headers)

bsObj = BeautifulSoup(req.text, 'lxml')
print(bsObj.find('table',{'class':'table-striped'}).get_text())

# 处理cookie(requests库不能执行javascript所以无法处理一些cookie)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('d:\\Anaconda\\Scripts\\chromedriver.exe',
                          options = chrome_options)
driver.get('http://www.baidu.com')
driver.implicitly_wait(1)
print(driver.get_cookies())

savedCookies = driver.get_cookies()

driver2 = webdriver.Chrome('d:\\Anaconda\\Scripts\\chromedriver.exe',
                          options = chrome_options)
driver2.get('http://www.baidu.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)
driver2.get('http://www.baidu.com')
driver2.implicitly_wait(1)
print(driver2.get_cookies())
driver.close()
driver2.close()

# 避免honey pot
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('d:\\Anaconda\\Scripts\\chromedriver.exe',
                          options = chrome_options)

driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')
for link in links:
    if not link.is_displayed():
        print('The link ' + link.get_attribute('href') + ' is a trap')

fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of ' + field.get_attribute('name'))
