import requests

import os

from . import config

class Client:
    def __init__(self, version=None):
        self.version = version

    def request(self, endpoint, params={}, headers={}, data={}, http_method='get'):
        headers['Accept'] = f'application/json;version={self.version}'
        r = requests.request(method=http_method, url=config.BASE_URL + endpoint, params=params, headers=headers, data=data)
        
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(f'Encountered status code {r.status_code}. See response below:\n{r.text}')
        
client = Client(config.VERSION)