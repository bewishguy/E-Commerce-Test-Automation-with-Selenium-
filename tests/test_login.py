import pytest
import time
from pages.login_page import LoginPage
from test_data.testdata_login import get_login_test_cases

@pytest.mark.parametrize("case", get_login_test_cases())
def test_login(driver, case):
    driver.get("https://automationexercise.com/login")
    page = LoginPage(driver)
    page.login(case["email"], case["password"])

    time.sleep(2)

    assert case["expected"] in driver.page_source
