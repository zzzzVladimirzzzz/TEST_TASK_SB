from urllib.parse import urljoin

import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _request(self, method, location, headers=None, data=None, params=None, allow_redirects=False,
                 jsonify=False, json=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects, json=json)

        if jsonify:
            json_response: dict = response.json()
            return json_response
        return response

    def get_http_bin(self):
        request = self._request(method='GET', location='get')
        return request

    def post_http_bin(self):
        request = self._request(method='POST', location='post')
        return request

    def get_http_bin_status(self, status_code: int):
        request = self._request(method='GET', location=f'status/{status_code}')
        return request

    def get_http_bin_delay(self, delay_time: int):
        request = self._request(method='GET', location=f'delay/{delay_time}')
        return request

    def get_http_bin_headers(self, freeform_value: str):
        request = self._request(method='GET', location=f'response-headers?freeform={freeform_value}')
        return request
