from faker import Faker

fake = Faker()


class Payloads:

    create_user = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name(),
        "nickname": fake.user_name()
    }