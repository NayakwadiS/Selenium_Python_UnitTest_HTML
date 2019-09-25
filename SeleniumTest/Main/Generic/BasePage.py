import time
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import datetime


class BasePage:
    timeout = 10

    LOCATORS = {
        'css': By.CSS_SELECTOR,
        'id': By.ID,
        'name': By.NAME,
        'xpath': By.XPATH,
        'link_text': By.LINK_TEXT,
        'partial_link_text': By.PARTIAL_LINK_TEXT,
        'tag': By.TAG_NAME,
        'class_name': By.CLASS_NAME
    }

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        if not instance:
            return None
        else:
            self.driver = instance.driver

    def find_element(self, *loc):
        # print(loc)
        return self.driver.find_element(*loc)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                self.locator_dictionary[what] = list(self.locator_dictionary[what])
                try:
                    self.locator_dictionary[what][0] = self.LOCATORS[self.locator_dictionary[what][0]]
                except KeyError:
                    raise KeyError("Please use a locator：'id_','name','class_name','css','xpath','link_text','partial_link_text'")
                self.locator_dictionary[what] = tuple(self.locator_dictionary[what])

                try:
                    element = WebDriverWait(self.driver,self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except Exception as e: #(TimeoutException,StaleElementReferenceException,NoSuchElementException,e):
                    self.captureLog(e, what)

                try:
                    element = WebDriverWait(self.driver,self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except (TimeoutException,StaleElementReferenceException) as e:
                    self.captureLog(e, what)

                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
                # self.locator = (self.LOCATORS[self.k], self.v)

        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    #@classmethod
    def captureLog(self,e,what):
        message = "An exception of type {0} occurred. With Element -:{1!r}".format(type(e).__name__, what)
        self.logger.error(message)
        self.now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/TestLogs/Failure-%s.png" %self.now)
        self.driver.quit()
        sys.exit("ERROR")

