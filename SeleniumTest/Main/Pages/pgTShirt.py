from seleniumpagefactory.Pagefactory import PageFactory


class TShirt(PageFactory):

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    locators = {
        "chkMedium": ('ID',"uniform-layered_id_attribute_group_2"),
        "chkSmall": ('ID', "uniform-layered_id_attribute_group_1"),
        "chkLarge": ('ID', "uniform-layered_id_attribute_group_3"),
        "chkColorOrange": ('ID', "layered_id_attribute_group_13"),
        "chkColorBlue": ('ID', "layered_id_attribute_group_14"),
        "chkCompositionsCotton": ('ID', "layered_id_feature_5"),
        "chkStyleGirly": ('ID', "layered_id_feature_13"),
        "imgTShirt": ('XPATH', "//h5/a[@title='Faded Short Sleeve T-shirts']")
    }

    def selectSizeMedium(self):
        self.chkMedium.click_button()
        self.logger.assert_step_log("PASS",'Successfully Selected size as "Medium".')

    def selectSizesmall(self):
        self.chkSmall.click_button()
        self.logger.assert_step_log("PASS",'Successfully Selected size as "Small".')

    def selectSizeLarge(self):
        self.chkLarge.click_button()
        self.logger.assert_step_log("PASS",'Successfully Selected size as "Large".')

    def selectOrangeColor(self):
        self.chkColorOrange.click()
        self.logger.assert_step_log("PASS",'Successfully Selected color as Orange for T-Shirt.')

    def selectBlueColor(self):
        self.chkColorBlue.click()
        self.logger.assert_step_log("PASS",'Successfully Selected color as Blue for T-Shirt.')

    def selectTShirt(self):
        self.imgTShirt.hover()
        self.imgTShirt.click()
        self.logger.assert_step_log("PASS",'Successfully Selected "Faded Short Sleeve T-shirts".')
