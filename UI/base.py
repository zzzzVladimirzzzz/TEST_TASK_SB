import pytest
from _pytest.fixtures import FixtureRequest

from fixtures import *


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.login_page: LoginPage = (
            request.getfixturevalue('login_page'))
