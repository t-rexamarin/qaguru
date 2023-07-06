import pytest
from selene import browser


@pytest.fixture(autouse=True)
def driver():
    browser.config.driver.maximize_window()
