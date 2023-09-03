from requests import Response

from utilities.base_api import BaseApi


class CatfactApi(BaseApi):
    def __init__(self):
        self.url = 'https://catfact.ninja/'

    def get_breeds(self) -> Response:
        """
        Get /breeds.
        """
        path = 'breeds'
        request = self._send_request(method='get', path=path)
        return request

    def get_facts(self) -> Response:
        """
        Get /facts.
        """
        path = 'facts'
        request = self._send_request(method='get', path=path)
        return request

    def get_fact(self) -> Response:
        """
        Get /fact.
        """
        path = 'fact'
        request = self._send_request(method='get', path=path)
        return request
