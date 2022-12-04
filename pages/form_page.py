import os
import random
import time
from calendar import monthrange

from selenium.webdriver.common.by import By

from generator.generators import value_subjects, generated_file, generator_person_us

from locators.form_page_locators import WebFormLocators
from pages.base_page import BasePage


class TextForm(BasePage):
    _locator = WebFormLocators()

    def fill_all_text_fields(self) -> tuple:
        self._remove_ads()
        person_info = next(generator_person_us())
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        mobile = "1005480054"
        current_address = person_info.current_address
        subjects = value_subjects[random.randint(0, len(value_subjects))]
        self._element_is_visible(self._locator.FIRST_NAME).send_keys(first_name)
        self._element_is_visible(self._locator.LAST_NAME).send_keys(last_name)
        self._element_is_visible(self._locator.EMAIL).send_keys(email)
        self._element_is_visible(self._locator.MOBILE).send_keys(mobile)
        self._element_is_visible(self._locator.SUBJECTS).send_keys(subjects)
        self._click_to_enter()
        self._element_is_visible(self._locator.ADDRESS).send_keys(current_address)
        return f"{first_name} {last_name}", email, mobile, subjects, current_address.replace("\n", " ")

    def select_random_month(self) -> tuple:
        self._element_is_visible(self._locator.DATE_OF_BIRTH_INPUT).click()
        month_num = random.randint(0, 11)
        random_month = self._element_are_visible(self._locator.SELECT_MONTH)[month_num]
        month = random_month.text
        random_month.click()
        return month, month_num

    def select_random_year(self) -> str:
        random_year = self._element_are_visible(self._locator.SELECT_YEAR)[random.randint(0, 200)]
        year = random_year.text
        random_year.click()
        return year

    def select_random_day(self, year, month) -> str:
        count_days = monthrange(year, month+1)[1]
        random_day = random.randint(1, count_days)
        if random_day > 9:
            day = f"0{random_day}"
        else:
            day = f"00{random_day}"
        element = self._driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day.react-datepicker__day--{day}")
        day = element.text
        self._click_to_element(element)
        return day

    def get_result_deta(self) -> str:
        element = self._element_is_present(self._locator.DATE_OF_BIRTH_INPUT).get_attribute('value')
        day = element.split()[0]
        month = element.split()[1]
        year = element.split()[2]
        return f"{int(day)} {month} {year}"

    def select_file(self) -> str:
        file_name, path = generated_file()
        self._element_is_present(self._locator.UPLOAD_PICTURE_BTN).send_keys(path)
        os.remove(path)
        return file_name.split("\\")[-1]

    def select_random_radio(self) -> str:
        element = self._element_is_present(self._locator.ALL_GENDER_RADIO)
        gender = element.text
        element.click()
        return gender

    def select_random_checkbox(self) -> str:
        element = self._element_is_present(self._locator.ALL_HOBBIES)
        hobbies = element.text
        element.click()
        return hobbies

    def select_state_and_city(self):
        state = self._element_is_visible(self._locator.SELECT_STATE_INPUT)
        self._click_to_element(state)
        self._click_to_arrow_down()
        self._click_to_enter()
        citi = self._element_is_visible(self._locator.SELECT_CITY_INPUT)
        self._click_to_element(citi)
        self._click_to_arrow_down()
        self._click_to_enter()

    def get_result_citi_state(self) -> str:
        elements = self._element_are_present(self._locator.RESULT_STATE_INPUT)
        state = elements[0].text
        citi = elements[1].text
        return f"{state} {citi}"

    def click_submit(self):
        self._go_to_element(self._element_is_visible(self._locator.SUBMIT))
        self._element_is_present(self._locator.SUBMIT).click()

    def get_result_table(self) -> list:
        result_list = self._element_are_visible(self._locator.RESULT_TABLE)
        data = []
        for item in result_list:
            self._go_to_element(item)
            data.append(item.text)
        return data