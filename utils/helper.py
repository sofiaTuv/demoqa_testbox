from faker import Faker

fake = Faker()


class Helper:

    @staticmethod
    def generate_name():
        return fake.name()

    @staticmethod
    def generate_email():
        return fake.email()

    @staticmethod
    def generate_address():
        return fake.address()
