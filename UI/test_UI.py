import pytest

from UI.base import BaseCase
from UI.locators.basic_locators import *
from static.creds import creds


@pytest.mark.UI
class TestUI(BaseCase):
    def test_login(self):
        self.login_page.login(login=creds[0], password=creds[1])
        self.login_page.find(LocatorsLoginPage.LOCATOR_PASSWORD_ERROR)
        try:
            assert LocatorsLoginPage.PASSWORD_ERROR_MESSAGE_RU in self.driver.page_source
        except AssertionError:
            assert LocatorsLoginPage.PASSWORD_ERROR_MESSAGE_CAPTCH in self.driver.page_source
