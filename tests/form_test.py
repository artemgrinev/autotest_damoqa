import time

import allure
from pytest_check import check
from pages.form_page import TextForm


@allure.suite("Registration Form")
class TestRegistrationForm:
    URL = "https://demoqa.com/automation-practice-form"

    @allure.feature('Filling out all forms')
    def test_registration_form(self, driver):
        registration_page = TextForm(driver, self.URL)
        registration_page.open()
        full_name, email, mobile, subjects, current_address = registration_page.fill_all_text_fields()
        date_value_before, date_value_after, date_value_select = registration_page.select_random_date()
        gender = registration_page.select_random_radio()
        hobbies = registration_page.select_random_checkbox()
        file_name = registration_page.select_file()
        registration_page.select_state_and_city()
        address = registration_page.get_result_citi_state()
        registration_page.click_submit()

        result_data = registration_page.get_result_table()
        selected_data = [full_name, email, gender, mobile, date_value_select, subjects,
                         hobbies, file_name, current_address, address]
        try:
            assert result_data == selected_data, "Received data does not match the selected"
        except AssertionError:
            for i in range(len(result_data)):
                with check:
                    assert result_data[i] == selected_data[i]

    @allure.feature('Selecting date')
    def test_select_date(self, driver):
        registration_page = TextForm(driver, self.URL)
        registration_page.open()
        date_value_before, date_value_after, date_value_select = registration_page.select_random_date()
        print(date_value_before, date_value_after, date_value_select)
        with check:
            assert date_value_before != date_value_after, "Date has not changed"
        with check:
            assert date_value_select == date_value_after, "The selected date does not match the received date"
