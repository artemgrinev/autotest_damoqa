from selenium.webdriver.common.by import By


class AutoCompleteLocator:
    MULTI_INPUT = (By.ID, "autoCompleteMultipleInput")
    MULTI_VALUE = (By.CLASS_NAME, "css-1rhbuit-multiValue auto-complete__multi-value")
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, '.css-1rhbuit-multiValue auto-complete__multi-value svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.ID, "autoCompleteSingleInput")


class DatePickerLocator:
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_AND_TIME_INPUT = (By.ID, "datePickerMonthYearInput")
    SELECT_MONTH = (By.CLASS_NAME, "react-datepicker__month-select")
    SELECT_YEAR = (By.CLASS_NAME, "react-datepicker__year-select")
    SELECT_DAYS_LIST = (By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day:not(.react-datepicker__day--outside-month)")

    DATE_AND_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    DATE_AND_TIME_MONTH = (By.CLASS_NAME, "react-datepicker__month-read-view")
    DATE_AND_TIME_YEAR = (By.CLASS_NAME, "react-datepicker__year-read-view")
    DATE_AND_TIME_TIME_LIST = (By.CLASS_NAME, "react-datepicker__time-list-item ")
    DATE_AND_TIME_MONTH_LIST = (By.CLASS_NAME, "react-datepicker__month-option")
    DATE_AND_TIME_YEAR_LIST = (By.CLASS_NAME, "react-datepicker__year-option")


class Sliderlocator:
    pass


class ProgressBarLocator:
    pass


class MenuLocator:
    pass
