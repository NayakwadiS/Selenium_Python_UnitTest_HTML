import os.path
import inspect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.options import Options as ie_options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings
from Main.Utility import xmlReader as Env
#import pytest
from Main.Utility import *
from pathlib import Path

class baseTest:
    driver = ""
    logger = HTMlLogger()

    def __init__(self):
        pass

    def TestCaseInit(self,f1_logger):
        self.f1_logger = f1_logger
        self.EnvironmentValue = Env.XmlReader()
        if self.EnvironmentValue.getValue("BrowserType") =="IE" :
            options = ie_options()
            options.ignore_protected_mode_settings = True
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True
            baseTest.driver = webdriver.Ie(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/MainResources/drivers/IEDriverServer.exe",options=options,capabilities=caps)
        else:
            options = Options()
            spath = str(Path(__file__).parent.parent.parent) + "\\testResources\\downloads\\"
            #print(spath)
            prefs = {"download.default_directory": spath,
                     "download.prompt_for_download": False,
                     "download.directory_upgrade": True}
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--headless")
            options.add_argument('--window-size=1420,1080')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            baseTest.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME,options=options)
            warnings.filterwarnings(action="ignore", message="unclosed",category=ResourceWarning)
            #baseTest.driver = webdriver.Chrome(str(Path(__file__).parent.parent.parent) + "/MainResources/drivers/chromedriver.exe",options=options)
        baseTest.driver.maximize_window()
        baseTest.driver.implicitly_wait(5)
        baseTest.driver.get(self.EnvironmentValue.getValue("Url"))
        # self.f1_logger.info("********************* test Script Starts %s ********************",inspect.stack()[2][3])
        # self.f1_logger.info("Successfully launch "+self.EnvironmentValue.getValue("BrowserType")+" Browser and navigated "
        #                     "to "+self.EnvironmentValue.getValue("Url"))

    @classmethod
    def getDriver(cls):
        return cls.driver

    def TestCaseExit(self,logger):
        self.driver.quit()
        # self.logger = logger
        # self.logger.close_report()
        logger.close_report()
        # self.logger.info("********************* test Case Exit ********************")

#B1=BaseTest()
