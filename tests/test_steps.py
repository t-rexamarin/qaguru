import allure
import pytest
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize(
    'driver',
    [
        'desktop'
        # (1920, 1080)
    ],
    indirect=True
)
def test_github_sign_in_desktop(driver):
    step_value = 'https://github.com'
    with allure.step(f"Открываем главную страницу {step_value}"):
        browser.open(step_value)

    step_value = 'Sign in'
    with allure.step("Ищем и нажимаем кнопку Sign in"):
        s(by.partial_text(step_value)).click()

    step_value = 'Sign in to GitHub'
    with allure.step(f"Открывается форма логина {step_value}"):
        s(by.text(step_value))



@pytest.mark.parametrize(
    'driver',
    [
        'mobile'
        # (1920, 1080)
    ],
    indirect=True
)
def test_github_sign_in_mobile(driver):
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