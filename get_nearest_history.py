from collections import OrderedDict
import urllib2
import os
import sys
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
os.environ['MOZ_HEADLESS'] = '1'
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
binary.add_command_line_options('-headless')
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(30)
base_url = "https://www.katalon.com/"
is_first_time = True
hash=OrderedDict()
# f1 = open("info-empire.txt", 'w')
# errorf = open("error-empire.txt", 'w')
driver.implicitly_wait(30)
print '1'
url = "https://csgoempire.com/history?seed=832"
driver.get(url)
if is_first_time:
    print '2'
    driver.find_element_by_link_text("Skip").click()
    is_first_time = False
print '3'
soup = BeautifulSoup(driver.page_source, 'html.parser')
print '4'
coins = soup.find_all('div',{'class':'coin'})
print 'processing: '+url
sc = ''
for coin in coins[::-1]:
    if 'coin-t' in str(coin):
        # f1.write('1')
        sc = sc + '1'

    else:
        if 'coin-ct' in str(coin):
            # f1.write('2')
            sc = sc + '2'
        else:
            sc = sc + '0'
            # f1.write('0')/
print sc
driver.quit()
print 'done: '+url
f = open('info-empire.txt','r')
s = f.readline()
print "Time black 2: " + str(s.count('2'))
print "Time orange 1: " + str(s.count('1'))
print "Time bonus 0: " + str(s.count('0'))
def substring_indexes(substring, string):
    """
    Generate indices of where substring begins in string

    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:
            break  # All occurrences have been found
        yield last_found
while True:
    count_1 = 0
    count_2 = 0
    count_0 = 0
    total = 0
    length = -30
    fall = False
    up = False
    while total == 0:
        ss = sc[length:]
        list_index = list(substring_indexes(ss, s))


        for i in list_index:
            if(s[i+len(ss)] is '1'):
                count_1 = count_1 + 1
            if(s[i+len(ss)] is '2'):
                count_2 = count_2 + 1
            if(s[i+len(ss)] is '0'):
                count_0 = count_0 + 1
            print "index "+str(i)+": "+s[i+len(ss)]
        total = count_0 + count_1 + count_2
        print "Find string "+ ss + " Total: "+ str(total)
        if total == 0 and not up:
            length = length + 1
            fall = True
            continue
        if total > 1 and not fall:
            length = length - 1
            up = True
            continue
        print count_0
        print count_1
        print count_2
        print "1: "+str((float)(count_1)/(count_1+count_0+count_2)*100)
        print "0: "+str((float)(count_0)/(count_1+count_0+count_2)*100)
        print "2: "+str((float)(count_2)/(count_1+count_0+count_2)*100)
        print "done"
        break
    next = raw_input("What is next round? 0:bonus 1:orange 2:black")
    sc = sc+next
