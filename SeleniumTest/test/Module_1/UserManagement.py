import unittest
#from six import with_metaclass
from Main.Generic import *
from Main.Pages import *
from Main.Utility import *
from ddt import ddt, data

def getData(fileName,TestCaseID):
    return ReadLine(fileName,TestCaseID)

@ddt
class UserManagement(unittest.TestCase,baseTest):
    logger = function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        #baseTest().__init__(self)
        baseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx",'test_SearchResults'))
    def test_add_delete_product_in_cart(self, currentRow):
        driver =baseTest().getDriver()

        with self.assertRaises(SystemExit) as cm:
           #Login In HR System
            pglogin=Login(driver,self.logger)
            pglogin.login()

           #navigateTo Admin
            pgHome=Home(driver,self.logger)
            pgHome.navigateToAdminPage()

            #search System User
            pgAdminUserManage=AdminUserManage(driver,self.logger)
            pgAdminUserManage.searchSystemUser(currentRow)

        self.assertEqual(cm.exception.code, "ERROR")
    # @data(getData("TestData.xlsx", 'SBI_blue_Chip'))
    # def test_2(self, search_values):
    #     print("In 2nd method")

    @classmethod
    def tearDown(cls):
        baseTest().TestCaseExit(cls.logger)
