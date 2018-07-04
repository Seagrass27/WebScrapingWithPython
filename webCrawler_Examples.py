from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('d:\\Anaconda\\scripts\\chromedriver.exe',
                          options = chrome_options)
driver.get('http://www.baidu.com')

inputField = driver.find_element_by_id('kw')
submitButton = driver.find_element_by_id('su')

inputField.send_keys('淘宝')
submitButton.click()

for h3 in driver.find_elements_by_tag_name('h3'):
    print(h3.text)
driver.close()
#---------------------------------------------------------------------
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('d:\\Anaconda\\scripts\\chromedriver.exe',
                          options = chrome_options)
driver.get('http://www.okooo.com/soccer/match/1000791/odds/')
target = driver.find_element_by_class_name('baidu_ad')
driver.execute_script("arguments[0].scrollIntoView();", target) 
#拖动到可见的元素去
from bs4 import BeautifulSoup
bsObj = BeautifulSoup(driver.page_source)
table = bsObj.find_all('tbody')[6]
content = []
for row in table.find_all('tr'):
    current_row = []
    for cell in row.find_all('td'):
        current_row.append(cell.get_text())
    content.append(current_row)
