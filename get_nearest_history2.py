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
ftest = open('test_empire.txt','r')
f = open('info-empire.txt','r')
s = f.readline()
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
total_bet = 0
bet_true = 0
total_bet = [0]*25
bet_true = [0]*25
before_lose = [False]*25
continue_lose = [0]*25
max_continue_lose = [0]*25
bet_true_above_70 = [0]*25
beted_above_70 = ['']*25
bet_above_70_false_before = [False]*25
bet_true_under_70 = [0]*25
bet_false_above_70 = [0]*25
bet_false_under_70 = [0]*25
bet_continue_false_above_70 = [0]*25
bet_continue_false_under_70 = [0]*25
max_continue_false_above_70 = [0]*25
max_continue_false_under_70 = [0]*25

bet_true_ct = [0]*25
bet_true_t = [0]*25
bet_true_bonus = [0]*25

bet_false_ct = [0]*25
bet_false_t = [0]*25
bet_false_bonus = [0]*25

bet_team = ['']*25

bet_ct_false_before = [False]*25
bet_t_false_before = [False]*25
bet_bonus_false_before = [False]*25

bet_ct_continue_lose = [0]*25
bet_t_continue_lose = [0]*25
bet_bonus_continue_lose = [0]*25

max_ct_continue_lose = [0]*25
max_t_continue_lose = [0]*25
max_bonus_continue_lose = [0]*25


#above-------------------
bet_above_true_ct = [0]*25
bet_above_true_t = [0]*25
bet_above_true_bonus = [0]*25

bet_above_false_ct = [0]*25
bet_above_false_t = [0]*25
bet_above_false_bonus = [0]*25

bet_above_team = ['']*25
bet_above_ct_false_before = [False]*25
bet_above_t_false_before = [False]*25
bet_above_bonus_false_before = [False]*25

bet_above_ct_continue_lose = [0]*25
bet_above_t_continue_lose = [0]*25
bet_above_bonus_continue_lose = [0]*25

max_above_ct_continue_lose = [0]*25
max_above_t_continue_lose = [0]*25
max_above_bonus_continue_lose = [0]*25

#under----------------
bet_under_true_ct = [0]*25
bet_under_true_t = [0]*25
bet_under_true_bonus = [0]*25

bet_under_false_ct = [0]*25
bet_under_false_t = [0]*25
bet_under_false_bonus = [0]*25

bet_under_team = ['']*25
bet_under_ct_false_before = [False]*25
bet_under_t_false_before = [False]*25
bet_under_bonus_false_before = [False]*25

bet_under_ct_continue_lose = [0]*25
bet_under_t_continue_lose = [0]*25
bet_under_bonus_continue_lose = [0]*25

max_under_ct_continue_lose = [0]*25
max_under_t_continue_lose = [0]*25
max_under_bonus_continue_lose = [0]*25


sc = ftest.readline()
bet_under_70_false_before = [False]*25
for next in sc:
    length = -25
    fall = False
    up = False
    bet = ['']*25
    beted = [False]*25
    text = s
    text_len = len(text)
    percent = 0.0
    for n in range(length,-1,1):
        ss = s[n:]
        list_index = list(substring_indexes(ss, text))
        count_1 = 0
        count_2 = 0
        count_0 = 0
        total = 0
        for i in list_index:
            if i+len(ss) == text_len:
                break;
            if(text[i+len(ss)] is '1'):
                count_1 = count_1 + 1
            if(text[i+len(ss)] is '2'):
                count_2 = count_2 + 1
            if(text[i+len(ss)] is '0'):
                count_0 = count_0 + 1
            # print "index "+str(i)+": "+text[i+len(ss)]
        total = count_0 + count_1 + count_2
        # if total == 0 and not up:
        #     length = length + 1
        #     fall = True
        #     continue
        # if total > 1 and not fall:
        #     length = length - 1
        #     up = True
        #     continue
        # print "Find string "+ ss + " Length: "+str(-n)+ " Total: "+ str(total)
        index = -n-1
        if total == 0:
            beted[index] = False
            beted_above_70[index] = ''
            bet_team[index]=''
            bet_above_team[index]= ''
            bet_under_team[index]=''
        else:
            # print "0: "+str(count_0)
            # print "1: "+str(count_1)
            # print "2: "+str(count_2)
            beted[index] = False
            if count_1 > count_2 and count_1 > count_0:
                bet[index] = '1'
                beted[index] = True
                percent = (float)(count_1) / total * 100
                if percent > 48.0:
                    beted_above_70[index] = 'above'
                    bet_above_team[index] = 't'
                    bet_under_team[index] = ''
                else:
                    beted_above_70[index] = 'under'
                    bet_under_team[index] = 't'
                    bet_above_team[index] = ''
                bet_team[index] = 't'
            if count_0 > count_1 and count_0 > count_2:
                bet[index] = '0'
                beted[index] = True
                percent = (float)(count_0) / total * 100
                if percent > 48.0:
                    beted_above_70[index] = 'above'
                    bet_above_team[index] = 'bonus'
                    bet_under_team[index] = ''
                else:
                    beted_above_70[index] = 'under'
                    bet_under_team[index] = 'bonus'
                    bet_above_team[index] = ''
                bet_team[index] = 'bonus'
            if count_2 > count_0 and count_2 >count_1:
                bet[index] = '2'
                beted[index] = True
                percent = (float)(count_2) / total * 100
                if percent > 48.0:
                    beted_above_70[index] = 'above'
                    bet_above_team[index] = 'ct'
                    bet_under_team[index] = ''
                else:
                    beted_above_70[index] = 'under'
                    bet_under_team[index] = 'ct'
                    bet_above_team[index] = ''
                bet_team[index] = 'ct'
            # print "1: "+str((float)(count_1)/(count_1+count_0+count_2)*100)
            # print "0: "+str((float)(count_0)/(count_1+count_0+count_2)*100)
            # print "2: "+str((float)(count_2)/(count_1+count_0+count_2)*100)
    for k in range(0,25,1):
        if beted[k]:
            total_bet[k] = total_bet[k] + 1
            if bet[k] == next:
                bet_true[k] = bet_true[k] + 1
                continue_lose[k] = 0
                before_lose[k] = False
                if bet_team[k] is 'ct':
                    bet_true_ct[k] = bet_true_ct[k] + 1
                    bet_ct_continue_lose[k] = 0
                    bet_ct_false_before[k] = False
                else:
                    if bet_team[k] is 't':
                        bet_true_t[k] = bet_true_t[k] + 1
                        bet_t_continue_lose[k] = 0
                        bet_t_false_before[k] = False
                    else:
                        if bet_team [k] is 'bonus':
                            bet_true_bonus[k] = bet_true_bonus[k] + 1
                            bet_bonus_continue_lose[k] = 0
                            bet_bonus_false_before[k] = False
                if bet_above_team[k] is 'ct':
                    bet_above_true_ct[k] = bet_above_true_ct[k] + 1
                    bet_above_ct_continue_lose[k] = 0
                    bet_above_ct_false_before[k] = False
                else:
                    if bet_above_team[k] is 't':
                        bet_above_true_t[k] = bet_above_true_t[k] + 1
                        bet_above_t_continue_lose[k] = 0
                        bet_above_t_false_before[k] = False
                    else:
                        if bet_above_team [k] is 'bonus':
                            bet_above_true_bonus[k] = bet_true_bonus[k] + 1
                            bet_above_bonus_continue_lose[k] = 0
                            bet_above_bonus_false_before[k] = False
                if bet_under_team[k] is 'ct':
                    bet_under_true_ct[k] = bet_under_true_ct[k] + 1
                    bet_under_ct_continue_lose[k] = 0
                    bet_under_ct_false_before[k] = False
                else:
                    if bet_under_team[k] is 't':
                        bet_under_true_t[k] = bet_under_true_t[k] + 1
                        bet_under_t_continue_lose[k] = 0
                        bet_under_t_false_before[k] = False
                    else:
                        if bet_under_team [k] is 'bonus':
                            bet_under_true_bonus[k] = bet_true_bonus[k] + 1
                            bet_under_bonus_continue_lose[k] = 0
                            bet_under_bonus_false_before[k] = False

                if beted_above_70[k] is 'above':
                    bet_true_above_70[k] = bet_true_above_70[k] + 1
                    bet_continue_false_above_70[k]=0
                    bet_above_70_false_before[k]=False
                if beted_above_70[k] is 'under':
                    bet_true_under_70[k] = bet_true_under_70[k] + 1
                    bet_continue_false_under_70[k] = 0
                    bet_under_70_false_before[k] = False
            else:
                before_lose[k]=True
                if bet_team[k] is 'ct':
                    bet_false_ct[k] = bet_false_ct[k] + 1
                    bet_ct_continue_lose[k] = bet_ct_continue_lose[k] + 1
                    if bet_ct_continue_lose[k] > max_ct_continue_lose[k]:
                        max_ct_continue_lose[k] = bet_ct_continue_lose[k]
                    bet_ct_false_before[k] = True
                else:
                    if bet_team[k] is 't':
                        bet_false_t[k] = bet_false_t[k] + 1
                        bet_t_continue_lose[k] = bet_t_continue_lose[k] + 1
                        if bet_t_continue_lose[k] > max_t_continue_lose[k]:
                            max_t_continue_lose[k] = bet_t_continue_lose[k]
                        bet_t_false_before[k] = True
                    else:
                        if bet_team[k] is 'bonus':
                            bet_false_bonus[k] = bet_false_bonus[k] + 1
                            bet_bonus_continue_lose[k] = bet_bonus_continue_lose[k] + 1
                            if bet_bonus_continue_lose[k] > max_bonus_continue_lose[k]:
                                max_bonus_continue_lose[k] = bet_bonus_continue_lose[k]
                            bet_bonus_false_before[k] = True
                if bet_above_team[k] is 'ct':
                    bet_above_false_ct[k] = bet_above_false_ct[k] + 1
                    bet_above_ct_continue_lose[k] = bet_above_ct_continue_lose[k] + 1
                    if bet_above_ct_continue_lose[k] > max_above_ct_continue_lose[k]:
                        max_above_ct_continue_lose[k] = bet_above_ct_continue_lose[k]
                    bet_above_ct_false_before[k] = True
                else:
                    if bet_above_team[k] is 't':
                        bet_above_false_t[k] = bet_above_false_t[k] + 1
                        bet_above_t_continue_lose[k] = bet_above_t_continue_lose[k] + 1
                        if bet_above_t_continue_lose[k] > max_above_t_continue_lose[k]:
                            max_above_t_continue_lose[k] = bet_above_t_continue_lose[k]
                        bet_above_t_false_before[k] = True
                    else:
                        if bet_above_team[k] is 'bonus':
                            bet_above_false_bonus[k] = bet_above_false_bonus[k] + 1
                            bet_above_bonus_continue_lose[k] = bet_above_bonus_continue_lose[k] + 1
                            if bet_above_bonus_continue_lose[k] > max_above_bonus_continue_lose[k]:
                                max_above_bonus_continue_lose[k] = bet_above_bonus_continue_lose[k]
                            bet_above_bonus_false_before[k] = True
                if bet_under_team[k] is 'ct':
                    bet_under_false_ct[k] = bet_under_false_ct[k] + 1
                    bet_under_ct_continue_lose[k] = bet_under_ct_continue_lose[k] + 1
                    if bet_under_ct_continue_lose[k] > max_under_ct_continue_lose[k]:
                        max_under_ct_continue_lose[k] = bet_under_ct_continue_lose[k]
                    bet_under_ct_false_before[k] = True
                else:
                    if bet_under_team[k] is 't':
                        bet_under_false_t[k] = bet_under_false_t[k] + 1
                        bet_under_t_continue_lose[k] = bet_under_t_continue_lose[k] + 1
                        if bet_under_t_continue_lose[k] > max_under_t_continue_lose[k]:
                            max_under_t_continue_lose[k] = bet_under_t_continue_lose[k]
                        bet_under_t_false_before[k] = True
                    else:
                        if bet_under_team[k] is 'bonus':
                            bet_under_false_bonus[k] = bet_under_false_bonus[k] + 1
                            bet_under_bonus_continue_lose[k] = bet_under_bonus_continue_lose[k] + 1
                            if bet_under_bonus_continue_lose[k] > max_under_bonus_continue_lose[k]:
                                max_under_bonus_continue_lose[k] = bet_under_bonus_continue_lose[k]
                            bet_under_bonus_false_before[k] = True

                if beted_above_70[k] is 'above':
                    bet_false_above_70[k] = bet_false_above_70[k] + 1
                    bet_continue_false_above_70[k] = bet_continue_false_above_70[k] + 1
                    if bet_continue_false_above_70[k] > max_continue_false_above_70[k]:
                         max_continue_false_above_70[k] = bet_continue_false_above_70[k]
                    bet_above_70_false_before[k] = True
                if beted_above_70 [k] is 'under':
                    bet_false_under_70[k] = bet_false_under_70[k] + 1
                    bet_continue_false_under_70[k] = bet_continue_false_under_70[k] + 1
                    if bet_continue_false_under_70[k] > max_continue_false_under_70[k]:
                         max_continue_false_under_70[k] = bet_continue_false_under_70[k]
                    bet_under_70_false_before[k] = True
                continue_lose[k] = continue_lose[k] + 1
                if continue_lose[k] > max_continue_lose[k]:
                    max_continue_lose[k] = continue_lose[k]
    s = s + next
for k in range(0,25,1):
    percent_above_70 = 0
    percent_under_70 = 0
    percent_ct = 0
    percent_t = 0
    percent_bonus = 0
    percent_above_ct = 0
    percent_above_t = 0
    percent_above_bonus = 0
    if bet_above_false_ct[k] != 0 or bet_above_true_ct[k] != 0:
        percent_above_ct= (float)(bet_above_true_ct[k])/(bet_above_true_ct[k]+bet_above_false_ct[k])*100
    if bet_above_false_t[k] != 0 or bet_above_true_t[k] != 0:
        percent_above_t= (float)(bet_above_true_t[k])/(bet_above_true_t[k]+bet_above_false_t[k])*100
    if bet_above_false_bonus[k] != 0 or bet_above_true_bonus[k] != 0:
        percent_above_bonus= (float)(bet_above_true_bonus[k])/(bet_above_true_bonus[k]+bet_above_false_bonus[k])*100
    percent_under_ct = 0
    percent_under_t = 0
    percent_under_bonus = 0
    if bet_under_false_ct[k] != 0 or bet_under_true_ct[k] != 0:
        percent_under_ct= (float)(bet_under_true_ct[k])/(bet_under_true_ct[k]+bet_under_false_ct[k])*100
    if bet_under_false_t[k] != 0 or bet_under_true_t[k] != 0:
        percent_under_t= (float)(bet_under_true_t[k])/(bet_under_true_t[k]+bet_under_false_t[k])*100
    if bet_under_false_bonus[k] != 0 or bet_under_true_bonus[k] != 0:
        percent_under_bonus= (float)(bet_under_true_bonus[k])/(bet_under_true_bonus[k]+bet_under_false_bonus[k])*100

    if bet_false_ct[k] != 0 or bet_true_ct[k] != 0:
        percent_ct= (float)(bet_true_ct[k])/(bet_true_ct[k]+bet_false_ct[k])*100
    if bet_false_t[k] != 0 or bet_true_t[k] != 0:
        percent_t= (float)(bet_true_t[k])/(bet_true_t[k]+bet_false_t[k])*100
    if bet_false_bonus[k] != 0 or bet_true_bonus[k] != 0:
        percent_bonus= (float)(bet_true_bonus[k])/(bet_true_bonus[k]+bet_false_bonus[k])*100
    if bet_false_above_70[k] != 0 or bet_true_above_70[k] != 0:
        percent_above_70 = (float)(bet_true_above_70[k])/(bet_true_above_70[k]+bet_false_above_70[k])*100
    if bet_false_under_70[k] != 0 or bet_true_under_70[k] != 0:
        percent_under_70 = (float)(bet_true_under_70[k])/(bet_true_under_70[k]+bet_false_under_70[k])*100
    if total_bet[k] != 0:
        print str(k)+": "+"Percent true: "+ str((float)(bet_true[k])/total_bet[k]*100) + ' Total bet: ' + str(total_bet[k]) + ' Max continue lose: ' + str(max_continue_lose[k])
        print str(k)+": "+'percent_above_ct: ' + str(percent_above_ct) + 'Total bet ct: ' + str(bet_above_true_ct[k] + bet_above_false_ct[k]) + ' Continue ct lose: ' + str(max_above_ct_continue_lose[k])
        print str(k)+": "+'44: ' + str(percent_above_t) + 'Total bet t: ' + str(bet_above_true_t[k] + bet_above_false_t[k]) + ' Continue t lose: ' + str(max_above_t_continue_lose[k])
        print str(k)+": "+'percent_above_bonus: ' + str(percent_above_bonus) + 'Total bet bonus: ' + str(bet_above_true_bonus[k] + bet_above_false_bonus[k]) + ' Continue bonus lose: ' + str(max_above_bonus_continue_lose[k])
        print str(k)+": " +'percent_under_ct: ' + str(percent_under_ct) + 'Total bet ct: ' + str(bet_under_true_ct[k] + bet_under_false_ct[k]) + ' Continue ct lose: ' + str(max_under_ct_continue_lose[k])
        print str(k)+": " +'percent_under_t: ' + str(percent_under_t) + 'Total bet t: ' + str(bet_under_true_t[k] + bet_under_false_t[k]) + ' Continue t lose: ' + str(max_under_t_continue_lose[k])
        print str(k)+": " +'percent_under_bonus: ' + str(percent_under_bonus) + 'Total bet bonus: ' + str(bet_under_true_bonus[k] + bet_under_false_bonus[k]) + ' Continue bonus lose: ' + str(max_under_bonus_continue_lose[k])
        print str(k)+": "+'Percent_ct: ' + str(percent_ct) + 'Total bet ct: ' + str(bet_true_ct[k] + bet_false_ct[k]) + ' Continue ct lose: ' + str(max_ct_continue_lose[k])
        print str(k)+": "+'Percent_t: ' + str(percent_t) + 'Total bet t: ' + str(bet_true_t[k] + bet_false_t[k]) + ' Continue t lose: ' + str(max_t_continue_lose[k])
        print str(k)+": "+'Percent_bonus: ' + str(percent_bonus) + 'Total bet bonus: ' + str(bet_true_bonus[k] + bet_false_bonus[k]) + ' Continue bonus lose: ' + str(max_bonus_continue_lose[k])
        print str(k)+": "+'Percent_abover 70: '+ str(percent_above_70) + 'Total bet > 70: '+str(bet_true_above_70[k]+bet_false_above_70[k])+' Continue > 70 lose: '+ str(max_continue_false_above_70[k])
        print str(k)+": "+'Percent_under 70: ' + str(percent_under_70) + 'Total bet < 70: ' + str(bet_true_under_70[k] + bet_false_under_70[k]) + ' Continue < 70 lose: ' + str(max_continue_false_under_70[k])
    else:
        print "Percent true of "+str(k)+": Not ready beted!"
