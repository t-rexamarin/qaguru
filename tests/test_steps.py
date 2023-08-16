import allure
import pytest

from selene import Browser
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


mobile = pytest.mark.parametrize('driver', [(412, 915), (390, 844)], ids=['412x915', '390x844'], indirect=True)
desktop = pytest.mark.parametrize('driver', [(1280, 1024), (1920, 1080)], ids=['1280x1024', '1920x1080'], indirect=True)


def is_desktop(driver: Browser):
    return driver.config.window_width > 1000


@desktop
# @mobile
def test_github_sign_in_desktop(driver):
    if not is_desktop(driver=driver):
        pytest.skip()

    pytest.mark.skipif(not is_desktop(driver))

    step_value = 'https://github.com'
    with allure.step(f"Открываем главную страницу {step_value}"):
        browser.open(step_value)

    step_value = 'Sign in'
    with allure.step("Ищем и нажимаем кнопку Sign in"):
        s(by.partial_text(step_value)).click()

    step_value = 'Sign in to GitHub'
    with allure.step(f"Открывается форма логина {step_value}"):
        s(by.text(step_value))


@mobile
# @desktop
def test_github_sign_in_mobile(driver):
    if is_desktop(driver=driver):
        pytest.skip()

    step_value = 'https://github.com'
    with allure.step(f"Открываем главную страницу {step_value}"):
        browser.open(step_value)

    with allure.step("Открываем боковое меню"):
        s('//button[@aria-label="Toggle navigation" and span[@class = "Button-content"]]').click()
        step_value = 'Sign in'
        with allure.step(f"Видим кнопку {step_value}"):
            sign_in_btn = s(by.partial_text(step_value))

    with allure.step(f"Нажимаем кнопку {step_value}"):
        sign_in_btn.click()

    step_value = 'Sign in to GitHub'
    with allure.step(f"Открывается форма логина {step_value}"):
        s(by.text(step_value))
