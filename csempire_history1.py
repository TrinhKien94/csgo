from collections import OrderedDict
import requests
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
# os.environ['MOZ_HEADLESS'] = '1'
# binary = FirefoxBinary(log_file=sys.stdout)
# binary.add_command_line_options('-headless')
# driver = webdriver.Firefox(firefox_binary=binary)
driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "https://www.katalon.com/"
is_first_time = True
hash=OrderedDict()
f1 = open("info-empire1.txt", 'w')
errorf = open("error-empire.txt", 'w')

for j in range(2064,2063,-1):
    try:
        driver.implicitly_wait(30)
        url = "https://csgoempire.com/history?seed="+str(j)
        driver.get(url)
        # if is_first_time:
        #     driver.find_element_by_link_text("Skip").click()
        #     is_first_time = False
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        coins = soup.find_all('img',{'class':'mb-1'})
        for coin in coins[::-1]:
            print(coin)
            if 'coin-t' in str(coin):
                f1.write('1')
            else:
                if 'coin-ct' in str(coin):
                    f1.write('2')
                else:
                    f1.write('0')
    except:
        errorf.write(url + "\n")
errorf.close()
f1.close()
