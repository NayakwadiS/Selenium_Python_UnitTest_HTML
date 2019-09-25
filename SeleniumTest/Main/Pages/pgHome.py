from seleniumpagefactory.Pagefactory import PageFactory


class Home(PageFactory):

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    locators = {
        "lnkDress": ('XPATH',"//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/*[@title='Dresses']"),
        "lnkWomen": ('XPATH', "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/*[@title='Women']"),
        "lnkCasualDress": ('XPATH',"//ul[@class='submenu-container clearfix first-in-line-xs']/li/a[text()='Casual Dresses']"),
        "lnkEveningDress":('XPATH',"//ul[@class='submenu-container clearfix first-in-line-xs']/li/a[text()='Evening Dresses']"),
        "lnkSummerDress": ('XPATH', "//ul[@class='submenu-container clearfix first-in-line-xs']/li/a[text()='Summer Dresses']"),
        "lnkTShirt": ('XPATH', "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/ul//a[@title='T-shirts']"),
        "lbTitle":('XPATH',"//title[text()='My Store']")

    }

    def navigateToCasualDress(self):
        #self.lbTitle.visibility_of_element_located()
        self.lnkDress.hover()
        self.lnkCasualDress.click_button()
        self.logger.assert_step_log("PASS",'Successfully Clicked on Casual Dress in Dress sub-menu.')

    def navigateToEveningDress(self):
        self.lbTitle.visibility_of_element_located()
        self.lnkDress.hover()
        self.lnkSummerDress.click_button()
        self.logger.assert_step_log("PASS",'Successfully Clicked on Evening Dress in Dress sub-menu.')

    def navigateToSummerDress(self):
        self.lbTitle.visibility_of_element_located()
        self.lnkDress.hover()
        self.lnkEveningDress.click_button()
        self.logger.assert_step_log("PASS",'Successfully Clicked on Summer Dress in Dress sub-menu.')

    def navigateToTshirts(self):
        self.lnkWomen.hover()
        self.lnkTShirt.click_button()
        self.logger.assert_step_log("PASS",'Successfully Clicked on T-shirts Menu.')
