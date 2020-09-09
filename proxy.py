from collections import OrderedDict
import requests
import os
import sys
import json
from bs4 import BeautifulSoup
from selenium import webdriver
def read_file_email():
    f = open("email_password.csv", "r")
    content = f.read()
    email_infos = content.split('\n')
    emails = []
    next_email = None
    for info in email_infos:
        if "|" not in  info:
            continue
        email, password, status = info.split('|')
        email_info = {"email":email, "password": password, "status": status}
        if status == '0' and next_email is None:
            next_email = email_info
            email_info["status"] = '1'
        emails.append(email_info)
    f.close()
    return emails, next_email

def save_file_email(emails):
    f = open("email_password.csv", "w")
    for email in emails:
        line = email["email"] + "|" +str(email["password"]) + "|" + str(email["status"])+'\n'
        f.write(line)
    f.close()
url = "http://localhost:8080/next"
response = requests.post(url)
proxy = response.json()
print(proxy)
emails, email = read_file_email()
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", proxy["ip"])
profile.set_preference("network.proxy.http_port", int(proxy["port"]))
profile.set_preference("network.proxy.ssl", proxy["ip"])
profile.set_preference("network.proxy.ssl_port", int(proxy["port"]))
profile.set_preference("general.useragent.override","whater_useragent")
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://www.okex.com/join/1/2336948')
driver.find_element_by_css_selector('.ok-auth-switch-login span:nth-child(2)').click()
driver.find_element_by_css_selector('.login-item-wrap .ok-auth-item:nth-child(1) input').send_keys(email["email"])
driver.find_element_by_css_selector('.login-item-wrap .ok-auth-item:nth-child(3) input').send_keys(email["password"])
driver.find_element_by_css_selector('.login-item-wrap .ok-auth-item:nth-child(4) input').send_keys(email["password"])
save_file_email(emails)


