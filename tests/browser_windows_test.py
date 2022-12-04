from pages.browser_windows_page import BrowserWindow


class TestBrowserWindow:
    def test_open_tab(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window("tab")
        assert text == "This is a sample page", "New tab has not opened"

    def test_open_window(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window("window")
        assert text == "This is a sample page", "New tab has not opened"
