# test_data/testdata_login.py
def get_login_test_cases():
    return [
        {
            "id": "TC01",
            "email": "",
            "password": "",
            "expected": "Email Address or Password incorrect"
        },
        {
            "id": "TC02",
            "email": "fakeemail@example.com",
            "password": "wrongpass",
            "expected": "Email Address or Password incorrect"
        },
        {
            "id": "TC03",  # ถูกต้อง
            "email": "your_registered_email@example.com",
            "password": "your_correct_password",
            "expected": "Logged in as"
        },
        {
            "id": "TC04",
            "email": "invalidemail.com",
            "password": "password",
            "expected": "Email Address or Password incorrect"
        },
    ]
