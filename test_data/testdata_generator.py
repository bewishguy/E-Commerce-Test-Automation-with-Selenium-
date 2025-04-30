from faker import Faker

faker = Faker()

def generate_signup_data():
    """สร้างข้อมูลสำหรับ Signup"""
    name = faker.name()
    email = faker.unique.email()
    password = faker.password(length=10)
    return {
        "name": name,
        "email": email,
        "password": password
    }

def generate_login_data(valid=True):
    """สร้างข้อมูลสำหรับ Login"""
    if valid:
        # จำลองว่าคุณจะใส่ login ที่ถูกต้อง (เช่น user ที่เพิ่ง signup มา)
        email = "testuser01@example.com"  # สมมุติอีเมลที่มีในระบบ
        password = "gtestpassword"         # สมมุติพาสเวิร์ดที่ถูกต้อง
    else:
        # ใส่อีเมลหรือพาสเวิร์ดผิด
        email = faker.email()
        password = faker.password(length=10)
    
    return {
        "email": email,
        "password": password
    }

# ทดสอบการสร้างข้อมูล
if __name__ == "__main__":
    signup_data = generate_signup_data()
    login_data_valid = generate_login_data(valid=True)
    login_data_invalid = generate_login_data(valid=False)

    print("=== Signup Data ===")
    print(signup_data)
    print("\n=== Valid Login Data ===")
    print(login_data_valid)
    print("\n=== Invalid Login Data ===")
    print(login_data_invalid)
