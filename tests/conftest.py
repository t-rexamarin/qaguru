import datetime

import pytest
from selene import browser, Browser
from qaguru.user import User, Hobbies


@pytest.fixture(scope='function', autouse=True)
def browser_setup() -> Browser:
    browser.driver.maximize_window()
    yield browser
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
