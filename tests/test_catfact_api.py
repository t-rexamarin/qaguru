import allure

from utilities import catfact_schemas


def test_get_breeds(catfact_api_fixture):
    with allure.step(f'Отправляем запрос get /breeds'):
        response = catfact_api_fixture.get_breeds()

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            catfact_api_fixture.validate_scheme(response=response, schema=catfact_schemas.breeds_success_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_get_facts(catfact_api_fixture):
    with allure.step(f'Отправляем запрос get /facts'):
        response = catfact_api_fixture.get_facts()

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            catfact_api_fixture.validate_scheme(response=response, schema=catfact_schemas.facts_success_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_get_fact(catfact_api_fixture):
    with allure.step(f'Отправляем запрос get /fact'):
        response = catfact_api_fixture.get_fact()

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            catfact_api_fixture.validate_scheme(response=response, schema=catfact_schemas.fact_success_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value
