import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(params=[(1280, 1024), (1920, 1080)], ids=['1280x1024', '1920x1080'])
def desktop_dimensions(request):
    return request.param


# @pytest.fixture(autouse=True, params=[(1280, 1024), (1920, 1080)])
# def driver(request):
#     width, height = request.param
#     options = webdriver.ChromeOptions()
#     options.add_argument(f"--window-size={width},{height}")
#     browser.config.driver_options = options
#     # browser.config.driver.maximize_window()
#     yield browser
#     browser.quit()


@pytest.fixture(autouse=True, params=['desktop', 'mobile'], ids=['desktop', 'mobile'])
def driver(request):
    options = webdriver.ChromeOptions()

    mode = request.param
    if mode == 'desktop':
        width, height = request.getfixturevalue('desktop_dimensions')
        options.add_argument(f"--window-size={width},{height}")
    if mode == 'mobile':
        mobile_emulation = {"deviceName": "Nexus 5"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)


    browser.config.driver_options = options
    # browser.config.driver.maximize_window()
    yield browser
    browser.quit()