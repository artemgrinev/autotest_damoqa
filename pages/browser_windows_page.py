import time

from selenium.webdriver.common.alert import Alert

from locators.browser_windows_locators import BrowserWindowsLocator, AlertPageLocator, FrameLocator, ModalDialogLocator
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


class FramePage(BasePage):
    _locator = FrameLocator()

    def check_frame(self, frame_num: str) -> list:
        if frame_num == "frame1":
            frame = self.element_is_visible(self._locator.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self._driver.switch_to.frame(frame)
            text = self.element_is_visible(self._locator.TEXT_FRAME).text
            self._driver.switch_to.default_content()
            return [width, height, text]
        if frame_num == "frame2":
            frame = self.element_is_visible(self._locator.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self._driver.switch_to.frame(frame)
            text = self.element_is_visible(self._locator.TEXT_FRAME).text
            self._driver.switch_to.default_content()
            return [width, height, text]


class ModalDialogPage(BasePage):
    _locator = ModalDialogLocator()

    def check_modal(self, small=False):
        if small:
            self.element_is_visible(self._locator.SMALL_BTN).click()
            modal_width = self.element_is_present(self._locator.MODAL).size.get("width")
            title_text = self.element_is_visible(self._locator.SM_TITLE_TEXT).text
            body_text = self.element_is_visible(self._locator.SM_BODY_TEXT).text
            return str(modal_width), title_text, str(len(body_text))
        else:
            self.element_is_visible(self._locator.LARGE_BTN).click()
            modal_width = self.element_is_present(self._locator.MODAL).size.get("width")
            title_text = self.element_is_visible(self._locator.TITLE_TEXT).text
            body_text = self.element_is_visible(self._locator.BODY_TEXT).text
            return str(modal_width), title_text, str(len(body_text))

