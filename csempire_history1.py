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
f1 = open("info-empire.txt", 'w')
errorf = open("error-empire.txt", 'w')

for j in range(0,831,1):
    try:
        driver.implicitly_wait(30)
        print '1'
        url = "https://csgoempire.com/history?seed="+str(j)
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
        for coin in coins[::-1]:
            if 'coin-t' in str(coin):
                f1.write('1')
            else:
                if 'coin-ct' in str(coin):
                    f1.write('2')
                else:
                    f1.write('0')
        print 'done: '+url
    except:
        print "error: "+url
        errorf.write(url + "\n")
errorf.close()
f1.close()
