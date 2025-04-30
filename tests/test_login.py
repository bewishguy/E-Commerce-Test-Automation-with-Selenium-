# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from testdata_generator import generate_login_data

@pytest.mark.parametrize("case", test_cases)
def test_login(driver, case):
    page = LoginPage(driver)
    page.login(case["email"], case["password"])

    if case["id"] == "TC03":
        assert "Home" in driver.title  # หรือเช็ค URL/text เฉพาะ
    else:
        assert case["expected"] in driver.page_source
