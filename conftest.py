import pytest
from selenium import webdriver
from helpers import user_data
from methods_api import API
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    print("\nstart browser for test..")
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture
def create_user():
    response = API.create_user(user_data)
    yield response, user_data
    API.delete_user(headers={"Authorization": response["accessToken"]})


@pytest.fixture
def login(driver, create_user):
    _, data = create_user
    user_email = data["email"]
    user_password = data["password"]
    page = MainPage(driver)
    page.open_main_page()
    page.click_my_account()
    page = LoginPage(driver)
    page.login_user(email=user_email, password=user_password)
