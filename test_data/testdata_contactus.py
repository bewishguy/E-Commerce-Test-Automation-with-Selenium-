from faker import Faker
import os

fake = Faker()

file_path = os.path.abspath("test_data/sample.txt")

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is a dummy file for testing upload.")

valid_contact_data = {
    "name": fake.name(),
    "email": fake.email(),
    "subject": fake.sentence(nb_words=4),
    "message": fake.text(),
    "file_path": file_path
}

# Invalid or missing field variants
missing_name_data = valid_contact_data.copy()
missing_name_data["name"] = ""

missing_email_data = valid_contact_data.copy()
missing_email_data["email"] = ""

invalid_email_data = valid_contact_data.copy()
invalid_email_data["email"] = "test@invalid"

missing_subject_data = valid_contact_data.copy()
missing_subject_data["subject"] = ""

missing_message_data = valid_contact_data.copy()
missing_message_data["message"] = ""
