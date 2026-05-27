import random
import string

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urls import DELETE_USER_URL, REGISTER_USER_URL


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser for tests: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "firefox":
        options = FirefoxOptions()
        web_driver = webdriver.Firefox(options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        web_driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Browser must be chrome or firefox")

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.fixture
def create_user():
    created_tokens = []

    def generate_user_data():
        suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return {
            "email": f"autotest_{suffix}@ya.ru",
            "password": f"Password_{suffix}",
            "name": f"User_{suffix}"
        }

    def _create_user():
        user_data = generate_user_data()
        response = requests.post(REGISTER_USER_URL, json=user_data)

        if response.status_code != 200:
            raise AssertionError(
                f"User was not created. Status code: {response.status_code}, body: {response.text}"
            )

        response_json = response.json()
        access_token = response_json.get("accessToken")

        if not access_token:
            raise AssertionError(
                f"No accessToken in response: {response.text}"
            )

        created_tokens.append(access_token)
        return user_data

    yield _create_user

    for token in created_tokens:
        requests.delete(
            DELETE_USER_URL,
            headers={"Authorization": token}
        )