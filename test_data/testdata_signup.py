from faker import Faker
import random

faker = Faker()

def generate_signup_data():
    return {
    "name": faker.first_name(),  # ชื่อ
    "email": faker.unique.email(),  # อีเมลไม่ซ้ำ (ใช้ unique)
    "password": faker.password(length=10),  # รหัสผ่านความยาว 10 ตัวอักษร
    "title": random.choice(["Mr", "Mrs"]),  # สุ่มเลือกคำนำหน้า
    "day": str(random.randint(1, 28)),  # วันที่เกิด (ใช้ 1-28 เพื่อหลีกเลี่ยงปัญหาเดือนสั้น)
    "month": random.choice([...]),  # สุ่มชื่อเดือน
    "year": str(random.randint(1970, 2000)),  # ปีเกิด
    "address": faker.street_address(),  # ที่อยู่
    "city": faker.city(),  # เมือง
    "country": random.choice([...]),  # ประเทศที่ dropdown มีให้เลือก
    "zipcode": faker.postcode(),  # รหัสไปรษณีย์
    "mobile": faker.phone_number()  # เบอร์โทร}
    }

    # return {
    #     "name" = data(["name"]),
    #     "email" = data(["email"]),
    #     "password": faker.password(length=10),
    #     "title": random.choice(["Mr", "Mrs"]),
    #     "day": str(random.randint(1, 28)),
    #     "month": random.choice(["January", "February", "March", "April", "May", "June",
    #                             "July", "August", "September", "October", "November", "December"]),
    #     "year": str(random.randint(1970, 2000)),
    #     "address": faker.street_address(),
    #     "city": faker.city(),
    #     "country": random.choice(["India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore" ]),
    #     "zipcode": faker.postcode(),
    #     "mobile": faker.phone_number()
    # }
