from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
import time

class MyAccount(PageFactory):

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    locators = {
        "btnCart": ('XPATH',"//*[@title='View my shopping cart']"),
        "btnOrderHistory" : ('XPATH',"//a[@title='Orders']"),
        "tblOrderHistory": ("XPATH", "//*[@id='order-list']/tbody")
    }

    def navigateToCart(self):
        # self.lnkWomen.hover()
        self.btnCart.click_button()
        self.logger.assert_step_log("PASS",'Successfully navigated to Cart...')

    def navigateToOrderHistory(self):
        # self.lnkWomen.hover()
        self.btnOrderHistory.click_button()
        self.logger.assert_step_log("PASS",'Successfully navigated to Order History...')

    def getHistoricalOrders(self):
        rows = self.tblOrderHistory.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
            # Get the columns (all the column 2)
            col = row.find_elements(By.TAG_NAME, "td")  # note: index start from 0, 1 is col 2
            col[5].click()
            self.logger.assert_step_log("PASS", 'Successfully verified Order History of '+ col[0].text)
            time.sleep(2)
            break
