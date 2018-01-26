from collections import OrderedDict
import urllib2
import json
from bs4 import BeautifulSoup
f1 = open('log_23.txt', 'w')
f2 = open('error.txt', 'w')
i=24
for j in range(1221168, 2560000, 1):
    if j%10000 == 0:
        f1.close()
        f1 = open('log_'+str(i)+'.txt', 'w')
        i = i + 1
    url ="http://www.wtfskins.com/crash/history/round/"+str(j)
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.text)
    except urllib2.HTTPError, e:
        f2.write(url)
        f2.write(e.fp.read())
f1.close()
f2.close()
    # page = urllib2.urlopen(url).read()
    # soup = BeautifulSoup("http://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/mega-6-45/winning-numbers/", 'html.parser')
    # soup = BeautifulSoup(page, 'json.parser')
    # print soup.text.encode('utf-8')
#     tags = soup.table.find_all('a')
#     results = soup.findAll("td", {"style": "text-align: center;"})
#     i = 0
#     for a in tags:
#         sum = 0
#         tongTungSo = 0
#         numbers = results[i].find_all('span')
#         resultNumber = ""
#         for number in numbers:
#             resultNumber += " " + number.string
#             tongTungSo += int(number.string[0]) + int(number.string[1])
#             sum += int(number.string)
#         resultNumber += " " + str(sum) + " " + str(tongTungSo)
#         # print resultNumber
#         # print a.string
#         dayResult[a.string] = resultNumber
#         i += 1
# for key, value in dayResult.items():
#     print key + value
