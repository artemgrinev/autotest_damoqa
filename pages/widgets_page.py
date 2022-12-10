import time
from calendar import monthrange
import random

from generator.generators import generated_date
from locators.widgets_locator import AutoCompleteLocator, DatePickerLocator, Sliderlocator, ProgressBarLocator, \
    MenuLocator
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    _locator = AutoCompleteLocator()
    pass


class DatePickerPage(BasePage):
    _locator = DatePickerLocator()

    def select_random_deta(self) -> tuple:
        date = next(generated_date())
        date_input = self.element_is_visible(self._locator.DATE_INPUT)
        date_value_before = date_input.get_attribute("value")
        date_input.click()
        self.set_element_by_visible_text(self._locator.SELECT_MONTH, date.date.strftime('%B'))
        self.set_element_by_visible_text(self._locator.SELECT_YEAR, str(date.date.year))
        self.click_on_the_selected_element(self._locator.SELECT_DAYS_LIST, str(date.date.day))
        date_value_after = date_input.get_attribute("value")
        return date_value_before, date_value_after, date.date.strftime("%m/%d/%Y")

    def click_on_the_selected_element(self, elements: tuple, value: str):
        item_list = self.element_are_visible(elements)
        for i in item_list:
            if i.text == value:
                i.click()
                break


class SliderPage(BasePage):
    _locator = Sliderlocator()
    pass


class ProgressBarPage(BasePage):
    _locator = ProgressBarLocator()
    pass


class MenuPage(BasePage):
    _locator = MenuLocator
    pass

