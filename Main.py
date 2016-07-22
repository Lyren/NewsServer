from bs4 import BeautifulSoup
from AndroidNews import *
import urllib2

# contentHtml = urllib2.urlopen('http://www.androidweekly.cn/tag/androiddevweekly/').read()
contentHtml = open('./Issue87.html')
soup = BeautifulSoup(contentHtml)


newsList = []

allOls = soup.find_all('ol')
allH3s = soup.find_all('h3')
allH3s.remove(allH3s[0])

i = 0
for ol in allOls:
    type = allH3s[i].string
    i = i + 1
    for li in ol.find_all('li'):
        news = AndroidNews(87,type)
        news.title = li.a.string
        news.link = li.a.get('href')
        ps = li.find_all('p')
        if ps.__len__() > 1:
            news.desc = ps[1].string
        newsList.append(news)

for n in newsList:
    print n.type
    print n.title
    print n.link
    print n.desc
