import pytest
from selene import browser, Browser
from qaguru.user import User


@pytest.fixture(scope='function', autouse=True)
def browser_setup() -> Browser:
    browser.driver.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def user_for_test() -> User:
    """
    Фикстура юзера для тестов.
    """
    user = User(
        full_name='тест тестович',
        email='test@test.ts',
        current_address='current address 1',
        permanent_address='permanent address 2',
    )
    return user
