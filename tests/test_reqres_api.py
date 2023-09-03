import allure

from utilities import reqres_schemas


def test_get_list_users(regres_api_fixture):
    step_value = 2
    with allure.step(f'Отправляем запрос get /api/users?page={step_value}'):
        response = regres_api_fixture.get_list_users(page=step_value)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.list_users_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_get_single_user(regres_api_fixture):
    step_value = 2
    with allure.step(f'Отправляем запрос get /api/users/{step_value}'):
        response = regres_api_fixture.get_single_user(user_id=step_value)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.single_user_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_get_list_resource(regres_api_fixture):
    with allure.step(f'Отправляем запрос get /api/unknown'):
        response = regres_api_fixture.get_list_resource()

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.list_resource_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_get_single_resource(regres_api_fixture):
    step_value = 2
    with allure.step(f'Отправляем запрос get /api/unknown/{step_value}'):
        response = regres_api_fixture.get_single_resource(resource_id=step_value)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.single_resource_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_post_create(regres_api_fixture):
    with allure.step(f'Отправляем запрос post /api/users'):
        name = "morpheus"
        job = "leader"
        payload = {
            "name": name,
            "job": job
        }
        # request_time = datetime.now().isoformat()
        response = regres_api_fixture.post_create(payload=payload)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            response_dict = regres_api_fixture.validate_scheme(
                response=response,
                schema=reqres_schemas.post_create_schema
            )

        step_value = 201
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value

        step_key = 'name'
        with allure.step(f'{step_key} = {name}'):
            assert response_dict[step_key] == name

        step_key = 'job'
        with allure.step(f'{step_key} = {job}'):
            assert response_dict[step_key] == job

        # step_key = 'createdAt'
        # with allure.step('Объект создан недавно'):
        #     response_time = parser.parse(response_dict[step_key])
        #     request_time = parser.parse(request_time)
        #     assert response_time >= request_time


def test_post_register_success(regres_api_fixture):
    with allure.step(f'Отправляем запрос post /api/register'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = regres_api_fixture.post_register(payload=payload)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.register_success_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_post_register_error(regres_api_fixture):
    with allure.step(f'Отправляем запрос post /api/register'):
        payload = {
            "email": "eve.holt@reqres.in"
        }
        response = regres_api_fixture.post_register(payload=payload)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            response_dict = regres_api_fixture.validate_scheme(
                response=response,
                schema=reqres_schemas.register_error_schema
            )

        step_value = 400
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value

        step_key = 'error'
        step_value = 'Missing password'
        with allure.step(f'{step_key} = {step_value}'):
            assert response_dict[step_key] == step_value


def test_post_login_success(regres_api_fixture):
    with allure.step(f'Отправляем запрос post /api/login'):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = regres_api_fixture.post_login(payload=payload)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            regres_api_fixture.validate_scheme(response=response, schema=reqres_schemas.login_success_schema)

        step_value = 200
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value


def test_post_login_error(regres_api_fixture):
    with allure.step(f'Отправляем запрос post /api/login'):
        payload = {
            "email": "eve.holt@reqres.in"
        }
        response = regres_api_fixture.post_login(payload=payload)

    with allure.step('Валидируем ответ'):
        with allure.step('Схема'):
            response_dict = regres_api_fixture.validate_scheme(
                response=response,
                schema=reqres_schemas.login_error_schema
            )

        step_value = 400
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value

        step_key = 'error'
        step_value = 'Missing password'
        with allure.step(f'{step_key} = {step_value}'):
            assert response_dict[step_key] == step_value


def test_delete_user(regres_api_fixture):
    step_value = 2
    with allure.step(f'Отправляем запрос delete /api/users/{step_value}'):
        response = regres_api_fixture.delete_user(user_id=step_value)

    with allure.step('Валидируем ответ'):
        step_value = 204
        with allure.step(f'Код ответа = {step_value}'):
            assert response.status_code == step_value
