from faker import Faker

fake = Faker()

payment_data = {
    "name_on_card": fake.name(),
    "card_number": "4111111111111111",
    "cvc": "123",
    "expiry_month": "12",
    "expiry_year": "2026"
}
