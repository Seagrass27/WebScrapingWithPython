import requests

params = {'firstname': 'Tyrell', 'lastname': 'Sun'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', 
                  data = params)
print(r.text) # r.text是string

#提交文件和图像
files = {'uploadFile': open('e:\照片\stewie.png', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', 
                  files = files)
print(r.text)

#登录和cookie
params = {'username': 'Tyrell', 'password':'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php',
                  params)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('------------')
print('Going to profile page...')
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',
                 cookies = r.cookies)
print(r.text)

#用session解决cookie
session = requests.Session()

params = {'username':'username','password':'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php',
                 params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('------------------')
print('Going to profile page...')
s = session.get('http://pythonscraping.com/page/cookies/profile.php')
print(s.text)

#HTTP基本接入认证
#from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Tyrell', 'password')
r = requests.post('http://pythonscraping.com/pages/auth/login.php',
                  auth = auth)
print(r.text)
