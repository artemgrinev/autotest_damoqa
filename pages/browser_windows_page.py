import time

from selenium.webdriver.common.alert import Alert

from locators.browser_windows_locators import BrowserWindowsLocator, AlertPageLocator
from pages.base_page import BasePage


class BrowserWindow(BasePage):
    _locator = BrowserWindowsLocator()

    def check_open_window(self, tab=False) -> str:
        if tab:
            self.element_is_visible(self._locator.TAB_BUTTON).click()
        else:
            self.element_is_visible(self._locator.WINDOW_BUTTON).click()
        self._driver.switch_to.window(self._driver.window_handles[1])
        text = self.element_is_visible(self._locator.TEXT).text
        return text


class AlertPage(BasePage):
    _locator = AlertPageLocator()

    def click_alert_btn(self) -> str:
        self.element_is_visible(self._locator.ALERT_BTN).click()
        text = Alert(self._driver).text
        Alert(self._driver).dismiss()
        return text

    def click_time_alert_btn(self) -> str:
        self.element_is_visible(self._locator.TIMER_ALERT_BTN).click()
        time.sleep(5)
        text = Alert(self._driver).text
        Alert(self._driver).dismiss()
        return text

    def click_confirm_btn(self, cancel_alert=False) -> str:
        self.element_is_visible(self._locator.CONFIRM_BTN).click()
        if cancel_alert:
            Alert(self._driver).dismiss()
        else:
            Alert(self._driver).accept()
        text = self.element_is_visible(self._locator.CONFIRM_RESULT).text
        return text
