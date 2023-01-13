import time

import pytest

from base import ApiBase
from static.data import *


@pytest.mark.API
class TestApi(ApiBase):

    def test_get_bin(self):
        assert self.get_request_bin().status_code == 200

    def test_post_bin(self):
        assert self.post_request_bin().status_code == 200

    def test_get_bin_status(self):
        assert self.get_bin_status(status_code=404).status_code == 404
        assert self.get_bin_status(status_code=-123).status_code == 502

    @pytest.mark.parametrize('delay_value, status_code',
                             [(delay_dict["value_negative"], 400), (delay_dict["value_2"], 200),
                              (delay_dict["value_3"], 200)])
    def test_get_bin_delay(self, delay_value, status_code):
        start_time = time.time()
        assert self.get_bin_delay(delay_time=delay_value).status_code == status_code
        assert time.time() - start_time > delay_value

    @pytest.mark.parametrize('form_value, status_code',
                             [(forms_dict["value"], 200), (forms_dict["value_1"], 200), (forms_dict["value_2"], 200)])
    def test_get_bin_headers(self, form_value, status_code):
        assert self.get_bin_headers(freeform_value=form_value).status_code == status_code
        assert self.get_bin_headers(freeform_value=form_value).headers['freeform'] == str(form_value)
