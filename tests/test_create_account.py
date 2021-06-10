import unittest

from data.constant import Constant
from webdriverfactory.web_driver_factory import WebDriverFactory



class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.driver = WebDriverFactory.get_driver(Constant.CHROME)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        print()

    def test_create_account(self):
        driver = self.driver
        driver.get(Constant.URL)