import random

from selenium.webdriver.common.by import By


class WebFormLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    ADDRESS = (By.ID, "currentAddress")

    # Date Of Birth
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")
    PREVIOUS_MONTH_BTN = (By.CSS_SELECTOR, "button[aria-label='Previous Month']")
    NEXT_MONTH_BTN = (By.CSS_SELECTOR, "button[aria-label='Next Month']")
    MONTH_DROP_DAWN = (By.CLASS_NAME, "react-datepicker__month-select")
    SELECT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']/option")
    YEAR_DROP_DAWN = (By.CLASS_NAME, "react-datepicker__year-select")
    SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']/option") # 201 years

    SUBJECTS = (By.ID, "subjectsInput")

    ALL_GENDER_RADIO = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1,3)}']")

    UPLOAD_PICTURE_BTN = (By.ID, "uploadPicture")

    ALL_HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1,3)}']")
    PICTURE = (By.CSS_SELECTOR, "")

    SELECT_STATE_INPUT = (By.ID, "react-select-3-input")
    RESULT_STATE_INPUT = (By.CLASS_NAME, "css-1uccc91-singleValue")
    SELECT_CITY_INPUT = (By.ID, "react-select-4-input")
    SUBMIT = (By.CSS_SELECTOR, '#submit')
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
    # RESULT_TABLE = (By.CSS_SELECTOR, ".table.table-dark > tbody > tr")