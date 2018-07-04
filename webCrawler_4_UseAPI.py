# =============================================================================
# Twitter API
# =============================================================================
from twitter import *

# go to https://apps.twitter.com/ to find Access token and Consumer Key, etc.
t = Twitter(auth = OAuth('2547164195-4vQKAa1dbnOi8WrIwTaNj3440TkLyBy6m9RJK26',
                         'inD4qk8ldHst51hQMZNeKn83OSyBCOeBqwiPJyIHPXLBX',
                         'MlKrD063LKLl20J8CP8jOAL9y',
                         'bBtV20DHSCKgGoSREsoUUK9fYRRkelK01C2LBcPWS5xw4rWrOr'))

# URLError was raised!
pythonTweets = t.search.tweets(q = '#python')
print(pythonTweets)           
           
statusUpdate = t.statuses.update(status = 'Testing API')
print(statusUpdate)

# =============================================================================
# 解析JSON数据
# =============================================================================
import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/' + 
                       ipAddress).read()
    responseJson = json.loads(response)
    print(type(responseJson))
    return responseJson.get('country_code')
print(getCountry('50.78.253.58'))