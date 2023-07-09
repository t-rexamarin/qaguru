import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    browser.config.driver_options = options
    browser.config.driver.maximize_window()
    yield browser
    browser.quit()
