from selenium.webdriver.common.by import By
from Main.Generic import *
#import time

class AdminUserManage(BasePage):

    def __init__(self,driver,logger):
        self.driver =driver
        self.logger=logger
        BasePage.__init__(self,driver,logger)

    locator_dictionary = {
        "edtUserName": (By.ID, 'searchSystemUser_userName'),
        "lstUserRole":(By.XPATH,"//select[@id='searchSystemUser_userType']"),
        "edtEmployeeName": (By.ID, "searchSystemUser_employeeName_empName"),
        "lstStatus": (By.XPATH, "//select[@id='searchSystemUser_status']"),
        "btnSearch": (By.NAME, "_search"),
        "lnkSearchResult": (By.NAME, "//table[@id='resultTable']//tr/td/a")
    }

    def searchSystemUser(self,currentRow):
        self.edtUserName.send_keys(currentRow.get("SystemUser"))
        self.logger.info("Enter System user name as "+currentRow.get("SystemUser"))

        super().selectElementByText(self.lstUserRole,currentRow.get("UserRole"))
        self.logger.info("Enter System user role as "+currentRow.get("UserRole"))

        self.edtEmployeeName.send_keys( currentRow.get("EmployeeName"))
        self.logger.info("Enter employee user name as "+currentRow.get("EmployeeName"))

        super().selectElementByText(self.lstStatus, currentRow.get("EmpStatus"))
        self.logger.info("Select Status as "+currentRow.get("EmpStatus"))

        self.btnSearch.click()
        self.logger.info("Successfully Click on Search button")

        super().waitAndAbort(self.lnkSearchResult)
        time.sleep(5)
