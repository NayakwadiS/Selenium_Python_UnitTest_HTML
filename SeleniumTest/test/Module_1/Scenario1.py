import unittest
from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility.logger import *
from Main.Utility import *
from ddt import ddt, data


def getData(fileName,TestCaseID):
    return ReadLine(fileName,TestCaseID)

@ddt
class Scenario1(unittest.TestCase,baseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        baseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx", 'test_Scenario1'))
    def test_Scenario1(self,currentRow):
        self.logger.assert_testcase_log("test_Scenario1")
        driver = baseTest().getDriver()
        try:
            pgHome = Home(driver,self.logger)
            pgHome.navigateToCasualDress()

            pgCasualDress = CasualDress(driver,self.logger)
            pgCasualDress.sortBy()
            pgCasualDress.selectSizeMedium()
            time.sleep(2)

            pgCasualDress.selectCasualDress()

            pgPrintedDress = PrintedDress(driver,self.logger)
            pgPrintedDress.selectQuantity(currentRow['Quntity'])
            pgPrintedDress.addItemToCart()
            pgPrintedDress.proceedToCheckOut()

            pgOrder = Order(driver,self.logger)
            pgOrder.deleteSingleItemFromCart()
            pgOrder.verifyEmptyCart()
        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        baseTest().TestCaseExit(cls.logger)
        # cls.logger.close_report()


if __name__ == "__main__":
    unittest.main()