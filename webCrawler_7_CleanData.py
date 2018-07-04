# =============================================================================
# 编写代码清洗数据
# =============================================================================
from urllib.request import urlopen
from bs4 import BeautifulSoup

def ngram(input_string,n):
    input_string = input_string.split(' ')
    output = []
    for i in range(len(input_string)-n+1):
        output.append(input_string[i:i+n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html)
content = bsObj.find('div',{'id':'mw-content-text'}).get_text()
ngrams = ngram(content,2)
print(ngrams)

# 移除转义字符\n，和unicode字符（先转换成bytes，再用ASCII转回str）
import re
def ngram(input_string, n):
    input_string = re.sub('\n+', ' ', input_string)
    input_string = re.sub(' +', ' ', input_string)
    input_string = input_string.encode('utf-8').decode('ascii','ignore')
    print(input_string)
    input_string = input_string.split(' ')
    output = []
    for i in range(len(input_string)-n+1):
        output.append(input_string[i:i+n])
    return output
ngrams = ngram(content,2)
print(ngrams)

# 进一步清洗，删除单字符的单词，除了'i'或'a';剔除在[]中的引用标记;剔除标点符号
import string
print(string.punctuation)
def cleanInput(input_string):
    input_string = re.sub('\n+', ' ', input_string)
    input_string = re.sub('\[[0-9]*\]', ' ', input_string)
    input_string = re.sub(' +', ' ', input_string)
    input_string = input_string.encode('utf-8').decode('ascii','ignore')
    cleaned_input = []
    input_string = input_string.split(' ')
    for word in input_string:
        word = word.strip(string.punctuation)
        if len(word) > 1 or word.lower() == 'a' or word.lower() == 'i':
            cleaned_input.append(word)
    return cleaned_input

def ngram(input_string, n):
    cleaned_input = cleanInput(input_string)
    output = []
    for i in range(len(cleaned_input)-n+1):
        output.append(cleaned_input[i:i+n])
    return output

ngrams = ngram(content, 2)
print(ngrams)

# =============================================================================
# 数据标准化
# =============================================================================

# 去重
from collections import OrderedDict
from collections import Counter

length = len(ngrams)
transform_ngrams = [tuple(i) for i in ngrams] #把ngrams中的每个list转成tuple，
                                              #不然无法用Counter，因为unhashable
ngrams = Counter(transform_ngrams)
ngrams_dict = dict(ngrams)
ngrams = OrderedDict(sorted(dict(ngrams).items(), key = lambda t: t[1], 
                            reverse = True))   
print(ngrams)

    

