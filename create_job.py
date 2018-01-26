# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://skinup.gg/")
        driver.find_element_by_xpath("//a[2]/div").click()
        driver.execute_script(driver,"var init_balance=parseInt($('.balance span').html());var balance=parseInt($('.balance span').html());$('#fakebet').val(0);$('.rolling-inner div').text();var is_lose=false;var bet_status='false';var bet_color='';var base_bet=8;var count_losed=0;var limit_losed=1;var total_bet_lost=0;var current_bet=0;var is_stop=false;var is_stop_green=false;var count_is_stop_green=4;var count_stop=4;function reset_bet(){bet_status='not';is_lose=false;count_losed=0;$('#fakebet').val(0);total_bet_lost=0;current_bet=0;count_losed=0}function calculateBetWhenLose(){current_bet=total_bet_lost*2}function update_win_lose(winner_temp){balance=parseInt($('.balance span').html());if(bet_color===winner_temp){is_lose=false;balance=balance+current_bet*2;reset_bet()}else{is_lose=true}}function setButtonActive(color){$('button[data-color='+color+']').click()}function do_bet(){console.log('do_bet\t'+bet_color);var color=bet_color.split('-')[1];setButtonActive(color);bet_status='true';$('#fakebet').val(current_bet);balance=balance-current_bet;socket.emit('roulette-bet',{color:Roulette.currentColor,value:current_bet});if(count_losed==limit_losed){socket.emit('roulette-bet',{color:0,value:2})}}function calculate_color_to_bet(){if($('.last')[0].className.split(' ')[1]=='color-1'){bet_color='color-1'}if($('.last')[0].className.split(' ')[1]=='color-2'){bet_color='color-2'}console.log('calculate_color_to_bet\t'+bet_color)}function check_same_color(){var one=$('.last')[0].className.split(' ')[1];var two=$('.last')[1].className.split(' ')[1];var three=$('.last')[2].className.split(' ')[1];var four=$('.last')[3].className.split(' ')[1];var five=$('.last')[4].className.split(' ')[1];var six=$('.last')[5].className.split(' ')[1];var seven=$('.last')[6].className.split(' ')[1];var eight=$('.last')[7].className.split(' ')[1];if(one==two){return true}return false}function update(){var time=Number($('.rolling-inner div').text().split(':')[0]);if($('.rolling-inner div').text()==='0:03'){bet_status='false'}if(time<14&&bet_status==='false'&&time>0){if(is_stop){if(count_stop==0){console.log('UnStop');is_stop=false;count_stop=3}else{reset_bet();count_stop=count_stop-1;console.log('Stop')}}if(is_stop_green){if(count_is_stop_green==0){console.log('UnStop Green');is_stop_green=false;count_is_stop_green=3}else{reset_bet();count_is_stop_green=count_is_stop_green-1;console.log('Stop Green')}}$('button[data-color='0']').click();balance=parseInt($('.balance span').html());console.log(bet_status);console.log(time);var winner_temp=$('.last')[0].className.split(' ')[1];if(winner_temp==='color-0'){is_stop_green=true;count_is_stop_green=2;reset_bet();return}if(current_bet>0&&!is_stop&&!is_stop_green)update_win_lose(winner_temp);if(balance>0&&!is_stop&&!is_stop_green){if(!is_lose){current_bet=base_bet;calculate_color_to_bet();console.log('Not lose\t'+bet_color);do_bet();bet_status='true';count_losed=0}else{count_losed=count_losed+1;total_bet_lost=total_bet_lost+current_bet;if(count_losed<=limit_losed){calculate_color_to_bet();calculateBetWhenLose();console.log(is_lose);console.log('Lose\t'+bet_color);do_bet();bet_status='true'}else{is_stop=true;count_stop=3;reset_bet()}}}else{reset_bet()}}}setInterval(update,1000);function reload(){location.reload()}setInterval(update,10000);")
        # ERROR: Caught exception [unknown command [executeScript]]
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
