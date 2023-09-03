import json

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl

from jsonschema.validators import validate
from requests import Response, Session, JSONDecodeError


class BaseApi:
    url: str

    @staticmethod
    def validate_scheme(response: Response, schema: dict) -> dict:
        """
        Validate response scheme.
        Response dictionary returns.
        """
        response_obj = json.loads(response.text)
        validate(instance=response_obj, schema=schema)
        return response_obj

    def _send_request(self, method: str, path: str, **kwagrs):
        url = self.url + path
        method = method.upper()
        with allure.step(f'{method} {url}'):
            with Session() as session:
                response = session.request(method=method, url=url, **kwagrs)
                request_curl = to_curl(request=response.request)
                allure.attach(
                    body=request_curl.encode('utf-8'),
                    name='Curl',
                    attachment_type=AttachmentType.TEXT,
                    extension='txt'
                )

                try:
                    json_response = response.json()
                except JSONDecodeError:
                    json_response = {}

                allure.attach(
                    body=json.dumps(json_response, indent=4).encode('utf-8'),
                    name='Response json',
                    attachment_type=AttachmentType.JSON,
                    extension='json'
                )
        return response
