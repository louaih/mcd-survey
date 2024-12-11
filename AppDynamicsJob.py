# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import sys

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://mcdvoice.com/")
        driver.find_element_by_id("header").click()
        driver.find_element_by_id("CN1").click()
        driver.find_element_by_id("CN1").clear()
        driver.find_element_by_id("CN1").send_keys("04705")
        driver.find_element_by_id("CN2").clear()
        driver.find_element_by_id("CN2").send_keys("16401")
        driver.find_element_by_id("CN3").clear()
        driver.find_element_by_id("CN3").send_keys("21124")
        driver.find_element_by_id("CN4").clear()
        driver.find_element_by_id("CN4").send_keys("13544")
        driver.find_element_by_id("CN5").clear()
        driver.find_element_by_id("CN5").send_keys("00059")
        driver.find_element_by_id("CN6").clear()
        driver.find_element_by_id("CN6").send_keys("9")
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("textR000455.1").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("textR004000.1").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR001000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000444']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000473']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000474']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR028000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR009000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000351']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR005000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//div[@id='FNSR000504']/span/span").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//div[@id='FNSR000509']/span/span").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000546']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR016000']/td[2]/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR018000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR019000']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("S081000").click()
        driver.find_element_by_id("S081000").clear()
        driver.find_element_by_id("S081000").send_keys("Lower the base cost of food! Disband the rewards program if necessary. I am hungry!")
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000345']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("textR020000.1").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("textR000387.5").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_xpath("//tr[@id='FNSR000482']/td/label").click()
        driver.find_element_by_id("NextButton").click()
        driver.find_element_by_id("NextButton").click()
    
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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

def parse_survey_code():


if __name__ == "__main__":

    unittest.main()
