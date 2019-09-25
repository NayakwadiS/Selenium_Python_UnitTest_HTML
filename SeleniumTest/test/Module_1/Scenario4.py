import unittest
from Main.Generic.BaseTest import *
from Main.Pages import *
from Main.Utility.logger import *
from Main.Utility import *
from ddt import ddt, data


def getData(fileName,TestCaseID):
    return ReadLine(fileName,TestCaseID)

@ddt
class Scenario4(unittest.TestCase,baseTest):
    logger = HTMlLogger()  # function_logger(logging.INFO, logging.ERROR)

    @classmethod
    def setUp(cls):
        baseTest().TestCaseInit(cls.logger)

    @data(getData("TestData.xlsx", 'test_Scenario4'))
    def test_Scenario4(self, currentRow):
        self.logger.assert_testcase_log("test_Scenario4")
        driver = baseTest().getDriver()
        try:
            pgHome = Home(driver,self.logger)
            pgHome.navigateToTshirts()

            pgTShirt = TShirt(driver,self.logger)
            pgTShirt.selectSizesmall()
            pgTShirt.selectTShirt()

            pgFadedTshirt = FadedTShirt(driver,self.logger)
            pgFadedTshirt.selectQuantity(currentRow['Quntity'])
            pgFadedTshirt.selectColor(currentRow['Color'])
            pgFadedTshirt.addItemToCart()
            pgFadedTshirt.proceedToCheckOut()

            pgOrder = Order(driver, self.logger)
            pgOrder.ProceedToCheckout()

            pglogin = Login(driver, self.logger)
            pglogin.signIn()

            # pgOrder.selectDeliveryAddrAsBillingAddr()
            pgOrder.ProceedToCheckoutInAddress()
            pgOrder.ProceedToCheckoutInShipping()
            pgOrder.verifyTermsOfServiceError()
            pgOrder.acceptTermsOfService()
            pgOrder.ProceedToCheckoutInShipping()
            pgOrder.selectPaymentMode(currentRow['Payment Mode'])
            pgOrder.confirmOrder()

        except Exception as e:
            self.logger.assert_step_fail_log(driver, str(e))

    @classmethod
    def tearDown(cls):
        baseTest().TestCaseExit(cls.logger)


if __name__ == "__main__":
    unittest.main()