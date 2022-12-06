from selenium.webdriver.common.by import By


class BrowserWindowsLocator:
    TAB_BUTTON = (By.ID, "tabButton")
    WINDOW_BUTTON = (By.ID, "windowButton")
    TEXT = (By.ID, "sampleHeading")


class AlertPageLocator:
    ALERT_BTN = (By.ID, "alertButton")
    TIMER_ALERT_BTN = (By.ID, "timerAlertButton")
    CONFIRM_BTN = (By.ID, "confirmButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMT_BTN = (By, "promtButton")


class FrameLocator:
    FIRST_FRAME = (By.ID, "frame1")
    SECOND_FRAME = (By.ID, "frame2")
    TEXT_FRAME = (By.ID, "sampleHeading")
