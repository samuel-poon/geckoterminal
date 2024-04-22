import requests

import os

from . import config

class Client:
    def __init__(self, version=None):
        self.version = version

    def request(self, endpoint, params={}, headers={}, data={}, http_method='get'):
        headers['Accept'] = f'application/json;version={self.version}'
        r = requests.request(method=http_method, url=config.BASE_URL + endpoint, params=params, headers=headers, data=data)
        
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError as e:
            raise requests.exceptions.JSONDecodeError(f'Encountered status code {r.status_code}. See response below:\n{r.text}', e.doc, e.pos)
        
client = Client(config.VERSION)