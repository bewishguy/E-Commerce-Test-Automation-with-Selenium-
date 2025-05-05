import time
import pytest
from pages.login_page import LoginPage
from test_data.testdata_login import (
    get_valid_login_data,
    get_invalid_email_login_data,
    get_wrong_password_data,
    get_empty_data,
    get_wrong_format_email_data
)

@pytest.mark.parametrize("data,expected_text", [
    (get_valid_login_data(), "Logged in as"),                                  # TC03
    (get_invalid_email_login_data(), "Your email or password is incorrect!"),  # TC04
    (get_wrong_password_data(), "Your email or password is incorrect!"),       # TC05
    (get_empty_data(), " "),                                                   # TC06
    (get_wrong_format_email_data(), "")                                        # TC07
    
])

def test_login(driver, data, expected_text):
    driver.get("https://automationexercise.com/login")
    
    page = LoginPage(driver)
    page.enter_email(data["email"])
    page.enter_password(data["password"])
    page.click_login()

    time.sleep(2)
    assert expected_text in driver.page_source
