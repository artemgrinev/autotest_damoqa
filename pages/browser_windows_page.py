from locators.browser_windows_locators import BrowserWindowsLocator
from pages.base_page import BasePage


class BrowserWindow(BasePage):
    _locator = BrowserWindowsLocator()

    def check_open_window(self, format_window: str) -> str:
        buttons = {"tab": self._locator.TAB_BUTTON,
                   "window": self._locator.WINDOW_BUTTON}
        self._element_is_visible(buttons.get(format_window)).click()
        self._driver.switch_to.window(self._driver.window_handles[1])
        text = self._element_is_visible(self._locator.TEXT).text
        return text
