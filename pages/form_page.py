import os
import random

import allure

from generator.generators import value_subjects, generated_file, generator_person_us, generated_date

from locators.form_page_locators import WebFormLocators
from pages.base_page import BasePage


class TextForm(BasePage):
    _locator = WebFormLocators()

    @allure.step("Fill in all text fields")
    def fill_all_text_fields(self) -> tuple:
        with allure.step("remove ads"):
            self.remove_ads()
        person_info = next(generator_person_us())
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        mobile = "1005480054"
        current_address = person_info.current_address
        subjects = value_subjects[random.randint(0, len(value_subjects))-1]
        with allure.step("Fill in all text fields"):
            self.element_is_visible(self._locator.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self._locator.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self._locator.EMAIL).send_keys(email)
            self.element_is_visible(self._locator.MOBILE).send_keys(mobile)
            self.element_is_visible(self._locator.SUBJECTS).send_keys(subjects)
            self.click_to_enter()
            self.element_is_visible(self._locator.ADDRESS).send_keys(current_address)
        return f"{first_name} {last_name}", email, mobile, subjects, current_address.replace("\n", " ")

    @allure.step("Select random date")
    def select_random_date(self):
        date = next(generated_date())
        date_input = self.element_is_visible(self._locator.DATE_INPUT)
        date_value_before = date_input.get_attribute("value")
        with allure.step("Click to button"):
            date_input.click()
        with allure.step("Select month"):
            self.set_element_by_visible_text(self._locator.SELECT_MONTH, date.date.strftime('%B'))
        with allure.step("Select year"):
            self.set_element_by_visible_text(self._locator.SELECT_YEAR, str(date.date.year))
        with allure.step("Select day"):
            self.click_on_the_selected_element(self._locator.SELECT_DAYS_LIST, str(date.date.day))
        date_value_after = date_input.get_attribute("value")
        return date_value_before, date_value_after, date.date.strftime("%d %B,%Y")

    @allure.step("Click on the selected element")
    def click_on_the_selected_element(self, elements: tuple, value: str):
        item_list = self.element_are_visible(elements)
        for i in item_list:
            if i.text == value:
                i.click()
                break

    @allure.step("Select file")
    def select_file(self) -> str:
        file_name, path = generated_file()
        self.element_is_present(self._locator.UPLOAD_PICTURE_BTN).send_keys(path)
        os.remove(path)
        return file_name.split("/")[-1]

    @allure.step("Select gendr radio button")
    def select_random_radio(self) -> str:
        element = self.element_is_present(self._locator.ALL_GENDER_RADIO)
        gender = element.text
        element.click()
        return gender

    @allure.step("Select hobbies checkbox")
    def select_random_checkbox(self) -> str:
        element = self.element_is_present(self._locator.ALL_HOBBIES)
        hobbies = element.text
        element.click()
        return hobbies

    @allure.step("Select  State and City")
    def select_state_and_city(self):
        state = self.element_is_visible(self._locator.SELECT_STATE_INPUT)
        with allure.step("State selection"):
            self.click_to_element(state)
            self.click_to_arrow_down()
            self.click_to_enter()
        citi = self.element_is_visible(self._locator.SELECT_CITY_INPUT)
        with allure.step("City selection"):
            self.click_to_element(citi)
            self.click_to_arrow_down()
            self.click_to_enter()

    @allure.step("Getting result state and city")
    def get_result_citi_state(self) -> str:
        elements = self.element_are_present(self._locator.RESULT_STATE_INPUT)
        state = elements[0].text
        citi = elements[1].text
        return f"{state} {citi}"

    @allure.step("Click submit button")
    def click_submit(self):
        self.go_to_element(self.element_is_visible(self._locator.SUBMIT))
        self.element_is_present(self._locator.SUBMIT).click()

    @allure.step("Getting table result")
    def get_result_table(self) -> list:
        result_list = self.element_are_visible(self._locator.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
