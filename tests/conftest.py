import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = options
    yield browser
    browser.quit()
