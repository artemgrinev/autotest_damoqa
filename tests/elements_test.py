import random

import allure
from pytest_check import check
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage
import time


@allure.suite("Elements")
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_fill_form()
            with check:
                assert full_name == output_name, "The full name does not match"
            with check:
                assert email == output_email, "The email does not match"
            with check:
                assert current_address == output_cur_addr, "The current address does not match"
            with check:
                assert permanent_address == output_perm_addr, "The permanent address does not match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_check_box()
            checked_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert checked_checkbox == output_result, "checkboxes have not been selected"

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title('Check radio button')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_random_radio_button("yes")
            output_yes = radio_button_page.get_result()
            radio_button_page.click_random_radio_button("no")
            output_no = radio_button_page.get_result()
            radio_button_page.click_random_radio_button("impressive")
            output_impressive = radio_button_page.get_result()
            with check:
                assert output_yes == "Yes", '"Yes" have not been selected'
            with check:
                assert output_impressive == "Impressive", '"Impressive" have not been selected'
            assert output_no == "No", '"No" have not been selected'

    @allure.feature("WebTable")
    class TestWebTable:
        @allure.title('Check add person')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            person = web_table_page.add_persons()
            full_people_list = web_table_page.check_added_person()
            assert person in full_people_list

        @allure.title('Check search person')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_persons()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in a table"

        @allure.title('Check update person info')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            row_to_search = web_table_page.add_persons()[random.randint(0, 5)]
            web_table_page.search_person(row_to_search)
            update_person = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert update_person in row, "no change has been made"

        @allure.title('Check delete person info')
        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_persons()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found", "Person is not deleted"

        @allure.title('checking the change in the number of rows')
        def test_change_count_of_rows(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            rows = web_table_page.select_up_to_row()
            result_rows = web_table_page.count_of_rows()
            assert rows == result_rows, "The number of rows does not match the specified"

    @allure.feature("TestButtons")
    class TestButtons:
        @allure.title('Check press button')
        def test_press_buttons(self, driver):
            button_page = ButtonPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            press_double_clk_btn = button_page.check_double_click()
            check_str_for_double_clk_btn = "You have done a double click"
            press_right_clk_btn = button_page.check_right_click()
            check_str_for_right_clk_btn = "You have done a right click"
            press_dynamic_clk_btn = button_page.check_dynamic_click()
            check_str_for_dynamic_clk_btn = "You have done a dynamic click"
            with check:
                assert press_double_clk_btn == check_str_for_double_clk_btn, "The double click button was not pressed"
            with check:
                assert press_right_clk_btn == check_str_for_right_clk_btn, "The right click button was not pressed"
            with check:
                assert press_dynamic_clk_btn == check_str_for_dynamic_clk_btn, "The click button was not pressed"

    @allure.feature("TestLinks")
    class TestLinks:
        @allure.title('Check open link')
        def test_open_links(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            status, href, element = links_page.good_request_get_status_code()
            url = links_page.open_windows_get_url(element)
            assert href == url, "the link will enter the correct url"

        @allure.title('Check status code')
        def test_request_code(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            good_status, good_request_href, element = links_page.good_request_get_status_code()
            no_content_status, no_content_href = links_page.no_content_get_status_code()
            created_status, created_href = links_page.created_get_status_code()
            not_found_status, not_found_href = links_page.not_found_get_status_code()
            with check:
                assert not_found_status == 404, f"when clicking on the link {not_found_href} received status 404"
            with check:
                assert created_status == 201, f"when clicking on the link {created_href} received status 201"
            with check:
                assert no_content_status == 204, f"when clicking on the link {no_content_href} received status 204"
            with check:
                assert good_status == 200, f"when clicking on the link {good_request_href} received status 200"
