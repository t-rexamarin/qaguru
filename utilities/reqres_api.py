from requests import Response

from utilities.base_api import BaseApi


class ReqresApi(BaseApi):
    def __init__(self):
        self.url = 'https://reqres.in/'

    def get_list_users(self, page: int = None) -> Response:
        """
        Get api/users.
        """
        path = 'api/users'
        if page:
            path += f'?page={page}'
        request = self._send_request(method='get', path=path)
        return request

    def get_single_user(self, user_id: int = 1) -> Response:
        """
        Get api/users/{user_id}.
        user_id = 1 by default.
        """
        path = f'api/users/{user_id}'
        request = self._send_request(method='get', path=path)
        return request

    def get_list_resource(self) -> Response:
        """
        Get api/unknown.
        """
        path = 'api/unknown'
        request = self._send_request(method='get', path=path)
        return request

    def get_single_resource(self, resource_id: int) -> Response:
        """
        Get api/unknown{resource_id}.
        """
        path = f'api/unknown/{resource_id}'
        request = self._send_request(method='get', path=path)
        return request

    def post_create(self, payload: dict) -> Response:
        """
        Post api/users.
        """
        path = 'api/users'
        request = self._send_request(method='post', path=path, data=payload)
        return request

    def put_create(self, user_id: int, payload: dict) -> Response:
        """
        Put api/users{user_id}.
        """
        path = f'api/users/{user_id}'
        request = self._send_request(method='post', path=path, data=payload)
        return request

    def delete_user(self, user_id: int):
        """
        Delete api/users/{user_id}.
        """
        path = f'api/users/{user_id}'
        request = self._send_request(method='delete', path=path)
        return request

    def post_register(self, payload: dict) -> Response:
        """
        Post api/register.
        """
        path = 'api/register'
        request = self._send_request(method='post', path=path, data=payload)
        return request

    def post_login(self, payload: dict) -> Response:
        """
        Post api/login.
        """
        path = 'api/login'
        request = self._send_request(method='post', path=path, data=payload)
        return request
