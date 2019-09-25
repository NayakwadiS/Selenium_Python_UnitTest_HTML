import pytest
from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility.htmllogger import HTMlLogger
# from test.Module_1 import *
#
# @pytest.fixture()
# def setup(request):
#     logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)
#     baseTest().TestCaseInit(logger)
#     request.instance.logger = logger
#     yield logger
#     baseTest().TestCaseExit(logger)



@pytest.mark.usefixtures("setup")
class TestScenario:
       # def __init__(self):
       #     print('start')

    def test_Scenario1(self):
        self.logger.assert_testcase_log("test_Scenario")
        driver = baseTest().getDriver()

        try:
            pgHome = Home(driver, self.logger)
            pgHome.navigateToCasualDress()

            pgCasualDress = CasualDress(driver, self.logger)
            pgCasualDress.selectSizeMedium()
            pgCasualDress.sortBy()
            pgCasualDress.selectCasualDress()

            pgPrintedDress = PrintedDress(driver, self.logger)
            pgPrintedDress.selectQuantity(self.currentRow['Quntity'])
            pgPrintedDress.addItemToCart()
            pgPrintedDress.proceedToCheckOut()

            pgOrder = Order(driver, self.logger)
            pgOrder.deleteSingleItemFromCart()
            pgOrder.verifyEmptyCart()
        except Exception as e:
            self.logger.assert_step_fail_log(driver,str(e))

        # pglogin.logout()

    def test_Scenario3(self):
        print(self.currentRow)              # get data from test case id in dic format
        self.logger.assert_testcase_log("test_Scenario3")
        driver = baseTest().getDriver()
        try:
            pglogin = Login(driver, self.logger)
            pglogin.login()

            pgMyAccount = MyAccount(driver, self.logger)
            pgMyAccount.navigateToOrderHistory()
            pgMyAccount.getHistoricalOrders()

            pglogin.logout()
        except Exception as e:
            self.logger.assert_step_fail_log(driver,str(e))
