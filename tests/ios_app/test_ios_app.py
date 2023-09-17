import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.ios
def test_search(ios_driver):
    with step('Нажимаем кнопку Text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    input_value = "hello@browserstack.com"
    with step(f'Вводим в поле {input_value}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type(input_value + "\n")

    with step(f'Проверяем что в блоке вывода отображается текст {input_value}'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text(input_value))

