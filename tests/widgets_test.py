from pages.widgets_page import DatePickerPage
from pytest_check import check


class TestAutoComplete:
    URL = "https://demoqa.com/auto-complete"
    pass


class TestDatePicker:
    URL = "https://demoqa.com/date-picker"

    def test_select_date(self, driver):
        page = DatePickerPage(driver, self.URL)
        page.open()
        date_value_before, date_value_after, date_value_select = page.select_random_deta()
        with check:
            assert date_value_before != date_value_after, "Date has not changed"
        with check:
            assert date_value_select == date_value_after, "The selected date does not match the received date"


class TestSlider:
    URL = "https://demoqa.com/slider"
    pass


class TestProgressBar:
    URL = "https://demoqa.com/progress-bar"
    pass


class TestMenu:
    URL = "https://demoqa.com/menu"
    pass
