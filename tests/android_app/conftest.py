import pytest
from appium import webdriver
from selene import browser

import project
from utils.attach import add_video


@pytest.fixture(scope='function')
def android_driver():
    browser.config.driver = webdriver.Remote(
        project.config.driver_remote_url,
        options=project.config.android_browserstack_options()
    )

    yield

    add_video(browser)
    browser.quit()
