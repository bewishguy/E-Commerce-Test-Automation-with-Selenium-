from faker import Faker
import random

faker = Faker()

def generate_signup_data():
    return {
    "name": faker.first_name(),
    "email": faker.unique.email(),
    "password": faker.password(length=10),  
    "title": random.choice(["Mr", "Mrs"]),  
    "day": str(random.randint(1, 28)),
    "month": random.choice([...]),  
    "year": str(random.randint(1970, 2000)),  
    "address": faker.street_address(),  
    "city": faker.city(), 
    "country": random.choice([...]),  
    "zipcode": faker.postcode(),  
    "mobile": faker.phone_number()  
    }
