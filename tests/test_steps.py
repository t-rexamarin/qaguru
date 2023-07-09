import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "t-rexamarin")
@allure.feature("Задачи в репозитории")
@allure.story("Находим в репозитории issue с номером 76")
def test_dynamic_steps():
    step_value = 'https://github.com'
    with allure.step(f"Открываем главную страницу {step_value}"):
        browser.open(step_value)

    step_value = 'eroshenkoam/allure-example'
    with allure.step(f"Ищем репозиторий {step_value}"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys(step_value)
        s("#query-builder-test").submit()

    step_value = 'eroshenkoam/allure-example'
    with allure.step(f"Переходим по ссылке репозитория {step_value}"):
        s(by.link_text(step_value)).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    step_value = '76'
    with allure.step(f"Проверяем наличие Issue с номером {step_value}"):
        s(by.partial_text(f"#{step_value}")).should(be.visible)
