import os
import random
import time
from calendar import monthrange

from selenium.webdriver.common.by import By

from generator.generators import value_subjects, generated_file, generator_person_us

from locators.form_page_locators import WebFormLocators
from pages.base_page import BasePage


class TextForm(BasePage):
    locator = WebFormLocators()

    def fill_all_text_fields(self) -> tuple:
        self.remove_ads()
        person_info = next(generator_person_us())
        first_name = person_info.firstname
        last_name = person_info.lastname
        email = person_info.email
        mobile = "1005480054"
        current_address = person_info.current_address
        subjects = value_subjects[random.randint(0, len(value_subjects))]
        self.element_is_visible(self.locator.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locator.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locator.EMAIL).send_keys(email)
        self.element_is_visible(self.locator.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locator.SUBJECTS).send_keys(subjects)
        self.click_to_enter()
        self.element_is_visible(self.locator.ADDRESS).send_keys(current_address)
        return f"{first_name} {last_name}", email, mobile, subjects, current_address.replace("\n", " ")

    def select_random_month(self) -> tuple:
        self.element_is_visible(self.locator.DATE_OF_BIRTH_INPUT).click()
        month_num = random.randint(0, 11)
        random_month = self.element_are_visible(self.locator.SELECT_MONTH)[month_num]
        month = random_month.text
        random_month.click()
        return month, month_num

    def select_random_year(self) -> str:
        random_year = self.element_are_visible(self.locator.SELECT_YEAR)[random.randint(0, 200)]
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
        element = self.driver.find_element(By.CSS_SELECTOR, f".react-datepicker__day.react-datepicker__day--{day}")
        day = element.text
        self.click_to_element(element)
        return day

    def get_result_deta(self) -> str:
        element = self.element_is_present(self.locator.DATE_OF_BIRTH_INPUT).get_attribute('value')
        day = element.split()[0]
        month = element.split()[1]
        year = element.split()[2]
        return f"{int(day)} {month} {year}"

    def select_file(self) -> str:
        file_name, path = generated_file()
        self.element_is_present(self.locator.UPLOAD_PICTURE_BTN).send_keys(path)
        os.remove(path)
        return file_name.split("\\")[-1]

    def select_random_radio(self) -> str:
        element = self.element_is_present(self.locator.ALL_GENDER_RADIO)
        gender = element.text
        element.click()
        return gender

    def select_random_checkbox(self) -> str:
        element = self.element_is_present(self.locator.ALL_HOBBIES)
        hobbies = element.text
        element.click()
        return hobbies

    def select_state_and_city(self):
        state = self.element_is_visible(self.locator.SELECT_STATE_INPUT)
        self.click_to_element(state)
        self.click_to_arrow_down()
        self.click_to_enter()
        citi = self.element_is_visible(self.locator.SELECT_CITY_INPUT)
        self.click_to_element(citi)
        self.click_to_arrow_down()
        self.click_to_enter()

    def get_result_citi_state(self) -> str:
        elements = self.element_are_present(self.locator.RESULT_STATE_INPUT)
        state = elements[0].text
        citi = elements[1].text
        return f"{state} {citi}"

    def click_submit(self):
        self.go_to_element(self.element_is_visible(self.locator.SUBMIT))
        self.element_is_present(self.locator.SUBMIT).click()

    def get_result_table(self) -> list:
        result_list = self.element_are_visible(self.locator.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data