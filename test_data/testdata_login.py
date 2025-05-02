from faker import Faker
import random

faker = Faker()

def generate_valid_login_data():
    return {
        "email": "testuser@example.com",
        "password": "CorrectPass123"
    }

def generate_invalid_email_data():
    return {
        "email": faker.unique.email(),  # อีเมลที่ไม่ตรงกับระบบ
        "password": "CorrectPass123"
    }

def generate_wrong_password_data():
    return {
        "email": "testuser@example.com",
        "password": faker.password(length=10)  # รหัสผ่านสุ่ม
    }

def generate_empty_fields_data():
    return {
        "email": "",
        "password": ""
    }

def generate_invalid_email_format_data():
    return {
        "email": "invalid-email-format",  # ไม่ถูกต้องตาม format
        "password": "CorrectPass123"
    }
