import pytest
from selene import browser


@pytest.fixture
def driver():
    browser.config.driver.maximize_window()
    return browser
