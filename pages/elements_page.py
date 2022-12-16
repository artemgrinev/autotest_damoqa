import random
import time

import allure
import requests
from selenium.webdriver.remote.webelement import WebElement

from generator.generators import generator_person_ru
from locators.element_page_locator import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablePageLocators, ButtonPageLocators, LinksPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    _locator = TextBoxPageLocators()

    @allure.step("Fill all text fields")
    def fill_all_fields(self) -> tuple:
        person_info = next(generator_person_ru())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step("filing fields"):
            self.element_is_visible(self._locator.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self._locator.EMAIL).send_keys(email)
            self.element_is_visible(self._locator.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self._locator.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Click button"):
            self.element_is_visible(self._locator.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check fill fields form")
    def check_fill_form(self) -> tuple:
        output_name = self.element_is_present(self._locator.CREATED_FULL_NAME).text.split(':')[1]
        output_email = self.element_is_present(self._locator.CREATED_EMAIL).text.split(':')[1]
        output_cur_addr = self.element_is_present(self._locator.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        output_perm_addr = self.element_is_present(self._locator.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return output_name, output_email, output_cur_addr, output_perm_addr


class CheckBoxPage(BasePage):
    _locator = CheckBoxPageLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        self.element_is_visible(self._locator.EXPAND_ALL_BUTTON).click()

    @allure.step("Click random check box")
    def click_random_check_box(self):
        item_list = self.element_are_visible(self._locator.ITEM_LIST)
        count = 21
        while count != 0:
            if count > 0:
                item = item_list[random.randint(1, 15)]
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("Checking with checkboxes have been selected")
    def get_checked_checkbox(self) -> str:
        checked_items = self.element_are_present(self._locator.CHECKED_ITEMS)
        data = [i.find_element("xpath", self._locator.TITLE_ITEM).text for i in checked_items]
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step("Getting output results")
    def get_output_result(self) -> str:
        result_list = self.element_are_present(self._locator.ITEM_LIST_OUTPUT)
        data = [i.text for i in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    _locators = RadioButtonLocators()

    @allure.step("Click random radio button")
    def click_random_radio_button(self, choice: str):
        choices = {"yes": self._locators.LABEL_YES,
                   "impressive": self._locators.LABEL_IMPRESSIVE,
                   "no": self._locators.LABEL_NO}
        self.element_is_visible(choices[choice]).click()

    @allure.step("Getting result")
    def get_result(self) -> str:
        return self.element_is_present(self._locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    _locator = WebTablePageLocators()

    @allure.step("Filled a text fild")
    def add_persons(self) -> list:
        count = 1
        while count != 0:
            person_info = next(generator_person_ru())
            first_name = person_info.firstname
            last_name = person_info.lastname
            email = person_info.email
            age = random.randint(14, 100)
            salary = random.randint(1000, 5000)
            departament = person_info.departament
            with allure.step("Filed"):
                self.element_is_visible(self._locator.ADD_BUTTON).click()
                self.element_is_visible(self._locator.FIRST_NAME_INPUT).send_keys(first_name)
                self.element_is_visible(self._locator.LAST_NAME_INPUT).send_keys(last_name)
                self.element_is_visible(self._locator.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self._locator.AGE_INPUT).send_keys(age)
                self.element_is_visible(self._locator.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self._locator.DEPARTAMENT_INPUT).send_keys(departament)
            with allure.step("Click button"):
                self.element_is_visible(self._locator.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), departament]

    @allure.step("Checking added person")
    def check_added_person(self) -> list:
        people_list = self.element_are_visible(self._locator.ALL_TABLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    @allure.step("Search person")
    def search_person(self, key_word: str):
        self.element_is_visible(self._locator.SEARCH_INPUT).send_keys(key_word)

    @allure.step("Checking search person")
    def check_search_person(self) -> list:
        delete_button = self.element_is_visible(self._locator.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self._locator.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("Update person info")
    def update_person_info(self) -> list:
        person_info = next(generator_person_ru())
        locators_dict = {"first_name": self._locator.FIRST_NAME_INPUT,
                         "last_name": self._locator.LAST_NAME_INPUT,
                         "email": self._locator.EMAIL_INPUT,
                         "age": self._locator.AGE_INPUT,
                         "salary": self._locator.SALARY_INPUT,
                         "departament": self._locator.DEPARTAMENT_INPUT
                         }
        person_info_dict = {"first_name": person_info.firstname,
                            "last_name": person_info.lastname,
                            "email": person_info.email,
                            "age": random.randint(14, 100),
                            "salary": random.randint(1000, 5000),
                            "departament": person_info.departament
                            }
        row_to_update = list(person_info_dict.keys())[random.randint(0, 5)]
        info_to_update = person_info_dict[row_to_update]
        with allure.step("Click update button"):
            self.element_is_visible(self._locator.UPDATE_BUTTON).click()
        time.sleep(3)
        with allure.step("Clear row"):
            self.element_is_visible(locators_dict[row_to_update]).clear()
        with allure.step("Filled"):
            self.element_is_visible(locators_dict[row_to_update]).send_keys(info_to_update)
        with allure.step("Click submit button"):
            self.element_is_visible(self._locator.SUBMIT_BUTTON).click()
        return info_to_update

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self._locator.DELETE_BUTTON).click()

    @allure.step("Checking delete person")
    def check_deleted(self):
        return self.element_is_present(self._locator.NO_FOUND).text

    @allure.step("Select up to row")
    def select_up_to_row(self) -> int:
        drop_dawn_page = self.element_is_visible(self._locator.ROW_PAGE_DROP_DAWN)
        self.go_to_element(drop_dawn_page)
        drop_dawn_page.click()
        list_rows = self.element_are_visible(self._locator.ROWS_TABLE_LIST)
        random_element = list(list_rows)[random.randint(0, 5)]
        random_element.click()
        return int(random_element.text.split()[0])

    @allure.step("Getting count of rows")
    def count_of_rows(self) -> int:
        all_rows = list(self.element_are_visible(self._locator.ROWS))
        return len(all_rows)


class ButtonPage(BasePage):
    _locator = ButtonPageLocators()

    @allure.step("Checking double click")
    def check_double_click(self) -> str:
        btn = self.element_is_visible(self._locator.DOUBLE_CLICK_BUTTON)
        self.double_click_action(btn)
        return self.element_is_visible(self._locator.DOUBLE_CLICK_MASSAGE).text

    @allure.step("Checking right click")
    def check_right_click(self) -> str:
        btn = self.element_is_visible(self._locator.RIGHT_CLICK_BUTTON)
        self.right_click_action(btn)
        return self.element_is_visible(self._locator.RIGHT_CLICK_MASSAGE).text

    @allure.step("Checking dynamic click")
    def check_dynamic_click(self) -> str:
        self.element_is_visible(self._locator.DYNAMIC_CLICK_BUTTON).click()
        return self.element_is_visible(self._locator.DYNAMIC_CLICK_MASSAGE).text


class LinksPage(BasePage):
    _locator = LinksPageLocators()

    @allure.step("Getting status code good requests")
    def good_request_get_status_code(self) -> tuple:
        element = self.element_is_visible(self._locator.SIMPLE_LINKS)
        href = element.get_attribute('href')
        status = requests.get(href).status_code
        return status, href, element

    @allure.step("Getting status code good link")
    def get_status_code_link(self, locator: tuple) -> tuple:
        element = self.element_is_visible(locator)
        href = f"https://demoqa.com/{element.get_attribute('id')}"
        status = requests.get(href).status_code
        return status, href

    @allure.step("Getting status code created")
    def created_get_status_code(self) -> tuple:
        status, href = self.get_status_code_link(self._locator.CREATED_LINKS)
        return status, href

    @allure.step("Getting status code no content")
    def no_content_get_status_code(self) -> tuple:
        status, href = self.get_status_code_link(self._locator.NO_CONTENT_LINKS)
        return status, href

    @allure.step("Getting status code bad requests")
    def bad_request_get_status_code(self) -> tuple:
        status, href = self.get_status_code_link(self._locator.BAD_REQUEST_LINKS)
        return status, href

    @allure.step("Getting status code not found")
    def not_found_get_status_code(self) -> tuple:
        status, href = self.get_status_code_link(self._locator.NOT_FOUND_LINKS)
        return status, href

    @allure.step("Checking open windows")
    def open_windows_get_url(self, element: WebElement) -> str:
        element.click()
        window_after = self._driver.window_handles[1]
        self._driver.switch_to.window(window_after)
        url = self._driver.current_url
        return url



