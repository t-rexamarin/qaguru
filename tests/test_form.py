import allure

from qaguru.practice_form import PracticeForm


def test_registration_form(user_data, browser_setup):
    practice_form = PracticeForm(browser=browser_setup)
    with allure.step("Открываем форму"):
        practice_form.open()

    with allure.step("Заполняем форму данными и отправляем"):
        practice_form.register(user=user_data)

    with allure.step("Проверить что форма успешно отправлена"):
        practice_form.should_have_registered(user=user_data)
