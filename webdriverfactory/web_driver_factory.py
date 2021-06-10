from data.constant import Constant
from selenium import webdriver
import chromedriver_autoinstaller


class WebDriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == Constant.CHROME:
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
        else:
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        return driver
