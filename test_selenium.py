# -*- coding: utf-8 -*-
from collections import OrderedDict
import urllib2
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "https://www.katalon.com/"
is_first_time = True
hash=OrderedDict()
f1 = open("info.txt",'w')
for j in range(285749,285049,-1):
    url = "https://www.wtfskins.com/crash/history/round/" + str(j)
    driver.get(url)
    if is_first_time:
        driver.find_element_by_xpath("//div[3]/button").click()
        driver.find_element_by_xpath("//div[2]/div/button").click()
        is_first_time = False
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data_container = soup.find('div',{'class':'data-container'})
    round_id = data_container.find("h2").text.replace("Round #","")
    table = data_container.find('table')
    tr_list = table.find_all('tr')
    day_of_month = tr_list[1].find_all('td')[1].text
    crash_point = tr_list[2].find_all('td')[1].text
    secret = tr_list[4].find_all('td')[1].text
    secret_badge = tr_list[5].find_all('td')[1].text
    secret_badge_index = tr_list[6].find_all('td')[1].text
    if hash.has_key(secret):
        hash[secret] = hash[secret] + 1
    else:
        hash[secret] = 1
    f1.write(round_id.encode('utf-8'))
    f1.write(day_of_month.encode('utf-8'))
    f1.write(crash_point.encode('utf-8'))
    f1.write(secret.encode('utf-8'))
    f1.write(secret_badge.encode('utf-8'))
    f1.write(secret_badge_index.encode('utf-8'))
    print round_id.encode('utf-8')
    print day_of_month.encode('utf-8')
    print crash_point.encode('utf-8')
    print secret.encode('utf-8')
    print secret_badge.encode('utf-8')
    print secret_badge_index.encode('utf-8')
    print ""
f = open("hash.txt","w")
for key, value in hash.items():
    f.write(key.encode('utf-8')+" "+str(value))
    print key.encode('utf-8')+" "+str(value)
f.close()
    # print round_id
