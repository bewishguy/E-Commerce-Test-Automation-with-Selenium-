from faker import Faker

faker = Faker()

def get_valid_login_data():
    return {
        "email": "bewishguy@gmail.com",  
        "password": "gtestpassword"
    }

def get_invalid_email_login_data():
    return {
        "email": "invalid_user@example.com",
        "password": faker.password()
    }

def get_wrong_password_data():
    return {
        "email": "validuser@example.com",
        "password": faker.password()
    }

def get_empty_data():
    return {
        "email": "",
        "password": ""
    }

def get_wrong_format_email_data():
    return {
        "email": "user123", # wrongemailformat
        "password": "gtestpassword"
    }
