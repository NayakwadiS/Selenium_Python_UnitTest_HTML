import time
import sys
import os
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class Wrappers:

    def __init__(self, driver, logger):
        self.driver = driver
        self.timeout = 10
        self.logger=logger

    def hover(self,element):
        ActionChains(self.driver).move_to_element(element).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def waitAndAbort(self, element):
        try:
            wait = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of(element)
            )
        except Exception as e:
            self.logger.error("An exception of type {0} occurred. With Element -:{1!r}".format(type(e).__name__, element))
            self.now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/TestLogs/Failure-%s.png" % self.now)
            self.driver.quit()
            sys.exit("ERROR")

    def selectElementByText(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    def click(self, element):
        element.click()

    def setText(self, element, text):
        element.send_keys(text)

    def getText(self, element):
        return element.text

