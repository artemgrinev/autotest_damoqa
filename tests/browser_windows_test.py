import allure

from pages.browser_windows_page import BrowserWindow, AlertPage, FramePage, ModalDialogPage
from pytest_check import check


@allure.suite("Browser windows")
class TestBrowserWindow:
    @allure.title("Open tab")
    def test_open_tab(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window(tab=True)
        assert text == "This is a sample page", "New tab has not opened"

    @allure.title("Open window")
    def test_open_window(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window()
        assert text == "This is a sample page", "New tab has not opened"


@allure.suite("Alert")
class TestAlert:
    @allure.title("Alert button")
    def test_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_alert_btn()
        assert text == "You clicked a button"

    @allure.title("Time alert button")
    def test_time_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_time_alert_btn()
        assert text == "This alert appeared after 5 seconds"

    @allure.title("Click ok button")
    def test_confirm_alert_click_ok_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn()
        assert text == "You selected Ok"

    @allure.title("Click no button")
    def test_confirm_alert_click_no_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn(cancel_alert=True)
        assert text == "You selected Cancel"


@allure.suite("Frame")
class TestFrame:

    @allure.title("Frame")
    def test_frame(self, driver):
        page = FramePage(driver, "https://demoqa.com/frames")
        page.open()
        result_frame1 = page.check_frame("frame1")
        result_frame2 = page.check_frame("frame2")
        with check:
            assert result_frame1 == ['500px', '350px', 'This is a sample page'], 'The frame does not exist'
        with check:
            assert result_frame2 == ['100px', '100px', 'This is a sample page'], 'The frame does not exist'


@allure.suite("Modal dialog")
class TestModalDialog:
    URL = "https://demoqa.com/modal-dialogs"

    @allure.title("Modal dialog")
    def test_modal_dialog(self, driver):
        page = ModalDialogPage(driver, self.URL)
        page.open()
        modal_width, title_text, len_body = page.check_modal()
        with check:
            assert modal_width == "800", "window size does not match"
        with check:
            assert title_text == "Large Modal"
        with check:
            assert len_body == "574"

    @allure.title("Small modal dialog")
    def test_small_modal_dialog(self, driver):
        page = ModalDialogPage(driver, self.URL)
        page.open()
        modal_width, title_text, body_text = page.check_modal(small=True)
        with check:
            assert modal_width == "300"
        with check:
            assert title_text == "Small Modal"
        with check:
            assert body_text == "47"
