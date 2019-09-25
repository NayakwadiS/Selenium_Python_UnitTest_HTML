import unittest
from Main.Generic.BaseTest import *
from Main.Pages.pgLogin import *
from Main.Utility.logger import *
from Main.Utility import *


class LoginTest(unittest.TestCase,baseTest):
    logger = function_logger(logging.INFO, logging.ERROR)
    htmllogger = HTMlLogger()

    @classmethod
    def setUp(cls):
        baseTest().TestCaseInit(cls.logger)

    def test_Login(self):
        self.htmllogger.assert_testcase_log("Login test")
        driver = baseTest().getDriver()
        try:
            pglogin = Login(driver,self.htmllogger)
            pglogin.login()
            pglogin.logout()
        except Exception as e:
            self.htmllogger.assert_step_fail_log(driver,str(e))


    @classmethod
    def tearDown(cls):
        baseTest().TestCaseExit(cls.htmllogger)

