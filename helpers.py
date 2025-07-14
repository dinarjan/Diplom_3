from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


def create_mail():
    mail = fake.email()
    return mail


def create_user_data():
    payload = {
        "email": f"{fake.email()}",
        "password": f"{fake.random_int()}",
        "name": f"{fake.first_name()}{fake.uuid4()}"
    }
    return payload


user_data = create_user_data()


def get_order_id(order_id):
    return (By.XPATH, f"//p[text()='{order_id}']")
