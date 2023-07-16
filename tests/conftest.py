import os
import datetime

import pytest
from dotenv import load_dotenv
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from qaguru.user import User, Hobbies
from qaguru.utils import attach, constants


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_setup() -> Browser:
    # browser.driver.maximize_window()
    browser_version = os.getenv(constants.BROWSER_VERSION)
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv(constants.LOGIN)
    password = os.getenv(constants.PASSWORD)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=driver))
    # browser.driver.maximize_window()
    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope='function')
def user_data():
    user = User(
        first_name='Имя',
        last_name='Фамилия',
        email='name@example.com',
        gender='Male',
        phone='7999555663',
        date_of_birth=datetime.date(year=1991, month=3, day=7),
        subjects_list=('Arts', 'History', 'Biology'),
        hobbies_list=(Hobbies.SPORT.value, Hobbies.READING.value, Hobbies.MUSIC.value),
        picture_name='Гигачад.jpg',
        address='Тестовая улица 1',
        state='NCR',
        city='Delhi'
    )
    return user
