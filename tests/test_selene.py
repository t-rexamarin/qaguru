import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


@allure.story("Находим в репозитории issue с номером 76")
def test_github(driver):
    driver.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
