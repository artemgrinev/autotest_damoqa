from locators.element_page_locator import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Artem')
        self.element_is_visible(self.locators.EMAIL).send_keys('artem@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('SPB')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Akademka')
        self.element_is_visible(self.locators.SUBMIT).click()