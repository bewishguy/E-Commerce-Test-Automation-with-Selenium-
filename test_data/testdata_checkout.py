from faker import Faker

fake = Faker()

checkout_comment_text = fake.sentence(nb_words=10)
