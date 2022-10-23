import random

from generator.generators import generator_person
from locators.element_page_locator import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_fill_form(self):
        output_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        output_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        output_cur_addr = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        output_perm_addr = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return output_name, output_email, output_cur_addr, output_perm_addr


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_check_box(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            if count > 0:
                item = item_list[random.randint(1, 15)]
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkbox(self):
        checked_items = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = [i.find_element("xpath", self.locators.TITLE_ITEM).text for i in checked_items]
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.element_are_present(self.locators.ITEM_LIST_OUTPUT)
        data = [i.text for i in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_random_radio_button(self, choice):
        choices = {"yes": self.locators.LABEL_YES,
                   "impressive": self.locators.LABEL_IMPRESSIVE,
                   "no": self.locators.LABEL_NO}
        self.element_is_visible(choices[choice]).click()

    def get_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_persons(self):
        count = 1
        while count != 0:
            person_info = next(generator_person())
            first_name = person_info.firstname
            last_name = person_info.lastname
            email = person_info.email
            age = random.randint(14, 100)
            salary = random.randint(1000, 5000)
            departament = person_info.departament
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(departament)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), departament]

    def check_added_person(self):
        people_list = self.element_are_visible(self.locators.ALL_TABLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data






