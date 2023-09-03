import pytest

from utilities.reqres_api import ReqresApi
from utilities.catfact_api import CatfactApi


@pytest.fixture(scope='session')
def regres_api_fixture():
    return ReqresApi()


@pytest.fixture(scope='session')
def catfact_api_fixture():
    return CatfactApi()
