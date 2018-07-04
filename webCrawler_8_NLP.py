# =============================================================================
# 概括数据
# =============================================================================
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

# 统计威廉哈里森总统就职演说2-gram的频率
def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]','', input)
    input = re.sub(' +', ' ', input)
    input = input.encode('utf=8').decode('ascii','ignore')
    cleanInput = []
    input = input.split(' ')
    for word in input:
        stripped_word = word.strip(string.punctuation)
        if (len(stripped_word) > 1 or stripped_word.lower() == 'i' or 
            stripped_word.lower() == 'a'):
            cleanInput.append(word.lower())
    return cleanInput

def ngram(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        temp = ' '.join(input[i:i+n])
        if temp not in output:
            output[temp] = 0
        output[temp] += 1
    return output

content = (urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').
           read().decode('utf-8'))
ngrams = ngram(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), 
                      reverse = True)
print(sortedNGrams)

# 去掉没意义的单词
def isCommon(ngram):
    commonWords = ['the','be','and','of','a','in','to','have','it','i','that',
                   'for','you','he','with','on','do','say','this','they','is',
                   'an','at','but','we','his','from','that','not','by','she',
                   'or','as','what','go','their','can','who','get','if','would',
                   'her','all','my','make','about','know','will','as','up',
                   'one','time','has','been','there','year','so','think','when',
                   'which','them','some','me','people','take','out','into',
                   'just','see','him','your','come','could','now','than','like',
                   'other','how','then','its','our','two','more','these','want',
                   'way','look','first','also','new','because','day','more',
                   'use','no','man','find','here','thing','give','many','well']
    for word in ngram:
        if word in commonWords:
            return True
    return False

def ngram(input, n): # 把检查常见词见到这个函数里
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        temp = ' '.join(input[i:i+n])
        check_common = isCommon(temp.split(' '))
        if check_common:
            continue
        else:
            if temp not in output:
                output[temp] = 0
            output[temp] += 1
    return output

ngrams = ngram(content,2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), 
                      reverse = True)
print(sortedNGrams)  
# 找到频率最高的2-gram出现的第一句话，可以归纳概括文章   
sentences = content.split('.')
top5_ngram = [sortedNGrams[i][0] for i in range(5)]

for ngram in top5_ngram:
    for sentence in sentences:
        if ngram in sentence.lower():
            print(sentence,'\n')
            break

# =============================================================================
# 马尔可夫模型
# =============================================================================

# 通过威廉哈里森就职演讲内容生成任意长度马尔可夫链组成的句子
from random import randint
from urllib.request import urlopen

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))#both ends included
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #去掉换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('"', '')
    #把标点和词分开，从而可以独立的作为单词
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text = text.replace(symbol, ' '+symbol+' ')
    words = text.split(' ')
    #过滤空字符
    words = [word for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    return wordDict

text = (urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').
        read().decode('utf-8'))
wordDict = buildWordDict(text)

#生成链长为100的马尔科夫链
length = 100
chain = ''
currentWord = 'I'
for i in range(length):
    chain += currentWord + ' '
    currentWord = retrieveRandomWord(wordDict[currentWord])
    
print(chain)

# =============================================================================
# 自然语言工具包
# =============================================================================
import nltk
nltk.download() #打开下载器
