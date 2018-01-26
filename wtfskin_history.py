# import urllib2
# from bs4 import BeautifulSoup
#https://www.wtfskins.com/crash/history/round/282820
#9034503bc4c6c1013ad71348b89a97a9
#0aef5d7190e2835774ca7fb0b7246717
#53e4ee67   b49f8edf 1622843512
#b4482b9e   a699ae7a 1617116471
#61cb9c86   cc0365ef -1782040937
#7f6ef166   fd937877 -2116323089


#53e4ee67a699ae7acc0365effd9378770aef5d7190e2835774ca7fb0b7246717
#1b241b8bbdce9abe19ff1e1c7a5630c8f18c1c36613522a44bc1a5c8
#53e4ee67   855b6c4f
# page = urllib2.urlopen('http://yahoo.com').read()
# soup = BeautifulSoup(page)
# soup.prettify()
# for anchor in soup.findAll('a', href=True):
#     print anchor['href']
from collections import OrderedDict
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
dayResult=OrderedDict()
for j in range(282392,282392,-1):
    url ="http://www.wtfskins.com/crash/history/round/"+str(j)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    print(url)
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.text)
    # table=soup.find("table").find_all('tr')
    # print(table[0].text)
    # value = crash_point_title.parent.findNext('td');
    # print(crash_point_title)
    # print (value.contents[0])
#     i=0
#     for a in tags:
#         sum =0
#         tongTungSo=0
#         numbers=results[i].find_all('span')
#         resultNumber=""
#         for number in numbers:
#             resultNumber += " "+number.string
#             tongTungSo += int(number.string[0])+int(number.string[1])
#             sum+=int(number.string)
#         resultNumber += " "+str(sum)+" "+str(tongTungSo)
#         # print resultNumber
#         # print a.string
#         dayResult[a.string]=resultNumber
#         i+=1
# for key, value in dayResult.items():
#     print key+value
