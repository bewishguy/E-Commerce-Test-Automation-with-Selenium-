# data/login_test_data.py
test_cases = [
    {
        "id": "TC03",
        "email": "bewishguy@gmail.com",
        "password": "gtestpassword",
        "expected": "Home",  # อาจใช้ตรวจ title หรือข้อความบนหน้า
    },
    {
        "id": "TC04",
        "email": "invalid_user@example.com",
        "password": "any_password",
        "expected": "Your email or password is incorrect!",
    },
    {
        "id": "TC05",
        "email": "bewishguy@gmail.com",
        "password": "wrong_password",
        "expected": "Your email or password is incorrect!",
    }
]