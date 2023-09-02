import json

from jsonschema.validators import validate
from requests import get, post, put, delete, Response


class ReqresApi:
    url: str

    def __init__(self):
        self.url = 'https://reqres.in/'

    def _get_to_reqres(self, path: str) -> Response:
        """
        Send get request.
        """
        url = self.url + path
        request = get(url=url)
        return request

    def _post_to_reqres(self, path: str, payload: dict) -> Response:
        """
        Send post request.
        """
        url = self.url + path
        request = post(url=url, json=payload)
        return request

    def _put_to_reqres(self, path: str, payload: dict) -> Response:
        """
        Send put request.
        """
        url = self.url + path
        request = put(url=url, json=payload)
        return request

    def _delete_to_reqres(self, path: str) -> Response:
        """
        Send delete request.
        """
        url = self.url + path
        request = delete(url=url)
        return request

    @staticmethod
    def validate_scheme(response: Response, schema: dict) -> dict:
        """
        Validate response scheme.
        Response dictionary returns.
        """
        response_obj = json.loads(response.text)
        validate(instance=response_obj, schema=schema)
        return response_obj

    def get_list_users(self, page: int = None) -> Response:
        """
        Get api/users.
        """
        path = 'api/users'
        if page:
            path += f'?page={page}'
        request = self._get_to_reqres(path=path)
        return request

    def get_single_user(self, user_id: int = 1) -> Response:
        """
        Get api/users/{user_id}.
        user_id = 1 by default.
        """
        path = f'api/users/{user_id}'
        request = self._get_to_reqres(path=path)
        return request

    def get_list_resource(self) -> Response:
        """
        Get api/unknown.
        """
        path = 'api/unknown'
        request = self._get_to_reqres(path=path)
        return request

    def get_single_resource(self, resource_id: int) -> Response:
        """
        Get api/unknown{resource_id}.
        """
        path = f'api/unknown/{resource_id}'
        request = self._get_to_reqres(path=path)
        return request

    def post_create(self, payload: dict) -> Response:
        """
        Post api/users.
        """
        path = 'api/users'
        request = self._post_to_reqres(path=path, payload=payload)
        return request

    def put_create(self, user_id: int, payload: dict) -> Response:
        """
        Put api/users{user_id}.
        """
        path = f'api/users/{user_id}'
        request = self._put_to_reqres(path=path, payload=payload)
        return request

    def delete_user(self, user_id: int):
        """
        Delete api/users/{user_id}.
        """
        path = f'api/users/{user_id}'
        request = self._delete_to_reqres(path=path)
        return request

    def post_register(self, payload: dict) -> Response:
        """
        Post api/register.
        """
        path = 'api/register'
        request = self._post_to_reqres(path=path, payload=payload)
        return request

    def post_login(self, payload: dict) -> Response:
        """
        Post api/login.
        """
        path = 'api/login'
        request = self._post_to_reqres(path=path, payload=payload)
        return request