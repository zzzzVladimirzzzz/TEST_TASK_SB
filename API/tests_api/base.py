import pytest


class ApiBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def get_request_bin(self):
        get_request_bin = self.api_client.get_http_bin()

        return get_request_bin

    def post_request_bin(self):
        post_request_bin = self.api_client.post_http_bin()
        return post_request_bin

    def get_bin_status(self, status_code: int):
        get_request_bin_status = self.api_client.get_http_bin_status(status_code=status_code)
        return get_request_bin_status

    def get_bin_delay(self, delay_time: int):
        get_request_bin_status = self.api_client.get_http_bin_delay(delay_time=delay_time)
        return get_request_bin_status

    def get_bin_headers(self, freeform_value: str):
        get_request_bin_headers = self.api_client.get_http_bin_headers(freeform_value=freeform_value)
        return get_request_bin_headers
