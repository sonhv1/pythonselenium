from datetime import datetime
from selenium.common import exceptions


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    @staticmethod
    def get_current_time():
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        return current_time

    def find_ele_by_css(self, css_selector):
        return self.driver.find_element_by_css(css_selector)

    def find_element_by_xpath(self, locator_xpath):
        return self.driver.find_element_by_xpath(locator_xpath)

    @staticmethod
    def click_elt_by_css(self, locator):
        return self.find_ele_by_css(locator).click()

    @staticmethod
    def clear_text(element):
        element.clear()

    def is_element_present_by_css(self, css_selector):
        try:
            self.find_ele_by_css(css_selector)
            # print("is_element_present_by_css + css_selector)
            return True
        except exceptions.NoSuchElementException as ex:
            # print("NoSuchElementException: " + str(ex))
            return False
