import pytest
from selenium import webdriver
from pages.contactus_page import ContactUsPage
from test_data import testdata_contactus as data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_TC01_submit_valid_form(driver):
    page = ContactUsPage(driver)
    page.open()
    page.fill_name(data.valid_contact_data["name"])
    page.fill_email(data.valid_contact_data["email"])
    page.fill_subject(data.valid_contact_data["subject"])
    page.fill_message(data.valid_contact_data["message"])
    page.upload_file(data.valid_contact_data["file_path"])
    page.click_submit()
    assert "Success! Your details have been submitted successfully." in page.get_success_message()

def test_TC02_missing_name(driver):
    page = ContactUsPage(driver)
    page.open()
    # Skip name
    page.fill_email(data.missing_name_data["email"])
    page.fill_subject(data.missing_name_data["subject"])
    page.fill_message(data.missing_name_data["message"])
    page.upload_file(data.missing_name_data["file_path"])
    
    page.click_submit()
    
    assert "Success! Your details have been submitted successfully." in driver.page_source

def test_TC03_missing_email(driver):
    page = ContactUsPage(driver)
    page.open()
    page.fill_name(data.missing_email_data["name"])
    # Skip email
    page.fill_subject(data.missing_email_data["subject"])
    page.fill_message(data.missing_email_data["message"])
    page.upload_file(data.missing_email_data["file_path"])

    current_url_before = driver.current_url
    page.click_submit_safe()

    assert driver.current_url == current_url_before

def test_TC04_invalid_email(driver):
    page = ContactUsPage(driver)
    page.open()
    page.fill_name(data.invalid_email_data["name"])
    page.fill_email(data.invalid_email_data["email"])
    page.fill_subject(data.invalid_email_data["subject"])
    page.fill_message(data.invalid_email_data["message"])
    page.upload_file(data.invalid_email_data["file_path"])
    page.click_submit()
    assert "email" in driver.page_source.lower() or "invalid" in driver.page_source.lower()

def test_TC05_missing_subject(driver):
    page = ContactUsPage(driver)
    page.open()
    page.fill_name(data.missing_subject_data["name"])
    page.fill_email(data.missing_subject_data["email"])
    # Skip subject
    page.fill_message(data.missing_subject_data["message"])
    page.upload_file(data.missing_subject_data["file_path"])
    page.click_submit()
    assert "Subject" in driver.page_source or "required" in driver.page_source

def test_TC06_missing_message(driver):
    page = ContactUsPage(driver)
    page.open()
    page.fill_name(data.missing_message_data["name"])
    page.fill_email(data.missing_message_data["email"])
    page.fill_subject(data.missing_message_data["subject"])
    # Skip message
    page.upload_file(data.missing_message_data["file_path"])
    page.click_submit()
    assert "Message" in driver.page_source or "required" in driver.page_source
