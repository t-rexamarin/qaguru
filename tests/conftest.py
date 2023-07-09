import pytest
from selene import browser, Browser

from demo_qa.user_class import User


@pytest.fixture(scope='function', autouse=True)
def browser_setup() -> Browser:
    browser.driver.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def user_data() -> User:
    user = User(
        first_name='Имя',
        last_name='Фамилия',
        email='name@example.com',
        gender='Male',
        phone='7999555663',
        day_of_birth='07',
        month_of_birth='March',
        year_of_birth='1991',
        subjects_list=('Arts', 'History', 'Biology'),
        hobbies_list=('Sports', 'Reading', 'Music'),
        picture_name='Гигачад.jpg',
        address='Тестовая улица 1',
        state='NCR',
        city='Delhi'
    )
    return user
