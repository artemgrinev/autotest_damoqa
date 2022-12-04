import time

from pages.form_page import TextForm


class TestRegistrationForm:
    def test_registration_form(self, driver):
        registration_page = TextForm(driver, "https://demoqa.com/automation-practice-form")
        registration_page.open()
        full_name, email, mobile, subjects, current_address = registration_page.fill_all_text_fields()
        month, month_num = registration_page.select_random_month()
        year = registration_page.select_random_year()
        day = registration_page.select_random_day(int(year), month_num)
        full_deta = f"{day} {month} {year}"
        gender = registration_page.select_random_radio()
        hobbies = registration_page.select_random_checkbox()
        file_name = registration_page.select_file()
        registration_page.select_state_and_city()
        address = registration_page.get_result_citi_state()
        registration_page.click_submit()

        result_data = registration_page.get_result_table()
        selected_data = [full_name, email, gender, mobile, full_deta, subjects,
                         hobbies, file_name, current_address, address]

        assert selected_data == result_data, "Полученная дата не соответствует выбранной"