from api.client import ApiClient
import pytest


@pytest.fixture(scope='session')
def api_client():
    return ApiClient(base_url='http://httpbin.org/')