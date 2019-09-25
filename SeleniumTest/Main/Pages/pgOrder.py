from seleniumpagefactory.Pagefactory import PageFactory
import time


class Order(PageFactory):

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    locators = {
        "btnDeleteFromCart": ('XPATH', "//a[@title='Delete']"),
        "lbEmptyCart": ('XPATH' , "//p[@class='alert alert-warning']"),
        "btnProceedToCheckout": ('XPATH', "//p/a[@title='Proceed to checkout']"),
        "chkDeliveryAddress": ('XPATH', "//p[@class='checkbox addressesAreEquals']/div"),
        "btnProceedAddress": ('XPATH', "//button[@name='processAddress']"),
        "btnProceedShipping": ('XPATH', "//button[@name='processCarrier']"),
        "chkTermsOfService1": ('ID', 'cgv'),
        "chkTermsOfService": ('XPATH','//label[contains(text(),"I agree to the terms of service")]'),
        "lblTermsOfServiceError":('XPATH', '//p[@class="fancybox-error"]'),
        "btnCloseTermsOfService": ('XPATH',"//a[@title='Close']"),
        "lnkPayByBank": ('XPATH',"//a[@title='Pay by bank wire']"),
        "btnConfirmOrder": ('XPATH', '//span[contains(text(),"I confirm my order")]'),
        "lbOrderConfirmation": ('XPATH',"//*[text()='Your order on My Store is complete.']")
    }

    def deleteSingleItemFromCart(self):
        self.btnDeleteFromCart.click_button()
        self.logger.assert_step_log("PASS",'Successfully Deleted Single Item from Cart .')

    def verifyEmptyCart(self):
        self.lbEmptyCart.visibility_of_element_located()
        self.logger.assert_step_log("PASS",'Successfully Verified Cart is Empty.')

    def ProceedToCheckout(self):
        self.btnProceedToCheckout.click_button()
        self.logger.assert_step_log("PASS",'Successfully Proceed To Checkout Items from Cart...')

    def selectDeliveryAddrAsBillingAddr(self):
        time.sleep(3)
        if not self.chkDeliveryAddress.is_Checked():
            self.chkDeliveryAddress.click_button()
        self.logger.assert_step_log("PASS",'Successfully selected Delivery Address As Billing Address.')

    def ProceedToCheckoutInAddress(self):
        self.btnProceedAddress.click_button()
        self.logger.assert_step_log("PASS",'Successfully Proceed To Checkout Items from Cart In Address Stage...')

    def ProceedToCheckoutInShipping(self):
        self.btnProceedShipping.hover()
        self.btnProceedShipping.click_button()
        self.logger.assert_step_log("PASS",'Successfully Proceed To Checkout Items from Cart In Shipping Stage...')

    def verifyTermsOfServiceError(self):
        self.lblTermsOfServiceError.visibility_of_element_located()
        self.btnCloseTermsOfService.click_button()
        self.logger.assert_step_log("PASS",'Successfully Terms of Service Error msg In Shipping Stage...')

    def acceptTermsOfService(self):
        # if not self.chkTermsOfService.isChecked() :
        time.sleep(2)
        self.chkTermsOfService.click_button()
        self.logger.assert_step_log("PASS",'Successfully Accepted Terms of Service In Shipping Stage.')

    def selectPaymentMode(self,sModeType):
        if "bank" in sModeType.lower():
            self.lnkPayByBank.click_button()
            self.logger.assert_step_log("PASS",'Successfully select Payment mode as "'+sModeType+'" In Payment Stage.')

    def confirmOrder(self):
        time.sleep(2)
        self.btnConfirmOrder.click_button()
        self.lbOrderConfirmation.visibility_of_element_located()
        self.logger.assert_step_log("PASS",'Order has been completed for Items in Cart.')
