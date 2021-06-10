from base_page import BasePage
from data.home_page_locators import HomePageLocator


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click_elt_by_css(HomePageLocator.sign_in_btn)

