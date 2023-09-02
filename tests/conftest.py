import pytest

from utilities.reqres_api import ReqresApi


@pytest.fixture(scope='session')
def api_fixture():
    return ReqresApi()
