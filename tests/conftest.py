import pytest
from selene import browser, Browser


@pytest.fixture()
def driver(request) -> Browser:
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


# @pytest.fixture(params=[(1280, 1024), (1920, 1080)], ids=['1280x1024', '1920x1080'])
# def desktop_config(request, driver):
#     width, height = request.param
#     driver.config.window_width = width
#     driver.config.window_height = height
#     yield driver
#
#
# @pytest.fixture(params=[(412, 915), (390, 844)], ids=['412x915', '390x844'])
# def mobile_config(request, driver):
#     width, height = request.param
#     driver.config.window_width = width
#     driver.config.window_height = height
#     yield driver
