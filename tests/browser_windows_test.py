from pages.browser_windows_page import BrowserWindow, AlertPage


class TestBrowserWindow:
    def test_open_tab(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window(tab=True)
        assert text == "This is a sample page", "New tab has not opened"

    def test_open_window(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window()
        assert text == "This is a sample page", "New tab has not opened"


class TestAlert:
    def test_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_alert_btn()
        assert text == "You clicked a button"

    def test_time_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_time_alert_btn()
        assert text == "This alert appeared after 5 seconds"

    def test_confirm_alert_click_ok_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn()
        assert text == "You selected Ok"

    def test_confirm_alert_click_no_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn(cancel_alert=True)
        assert text == "You selected Cancel"
