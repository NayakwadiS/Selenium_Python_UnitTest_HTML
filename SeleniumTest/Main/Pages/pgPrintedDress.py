from seleniumpagefactory.Pagefactory import PageFactory


class PrintedDress(PageFactory):

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    locators = {
        "edtQuantity": ('ID',"quantity_wanted"),
        "lstSize": ('ID', "group_1"),
        "btnAddToCart": ('ID', "add_to_cart"),
        "btnContinueShopping" : ('XPATH',"//*[@title='Continue shopping']"),
        "btnProceedToCheckout": ('XPATH', "//a[@title='Proceed to checkout']")
    }

    def selectQuantity(self,iQuantity):
        self.edtQuantity.clear_text()
        self.edtQuantity.set_text(iQuantity)
        self.logger.assert_step_log("PASS",'Successfully Selected Quantity as '+iQuantity+'.')

    def selectSize(self,iSize):
        self.lstSize.select_element_by_text(iSize)
        self.logger.assert_step_log("PASS",'Successfully Selected Size as ' + iSize + '.')

    def addItemToCart(self):
        self.btnAddToCart.click_button()
        self.logger.assert_step_log("PASS",'Successfully Added Selected Item to Cart .')

    def ContinueShopping(self):
        self.btnContinueShopping.click_button()
        self.logger.assert_step_log("PASS",'click on Continue Shopping...')

    def proceedToCheckOut(self):
        self.btnProceedToCheckout.click_button()
        self.logger.assert_step_log("PASS",'Successfully click on Proceed To Checkout .')
