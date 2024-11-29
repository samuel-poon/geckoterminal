import requests

from typing import Optional

from . import config

class RequestExecutor:
    def __init__(
            self,
            version: Optional[str] = None
        ):
        self.version = version

    def request(
            self,
            endpoint: str,
            params: dict        = {},
            headers:dict        = {},
            data:dict           = {},
            http_method: str    = 'get'
        ):

        headers['Accept'] = f'application/json;version={self.version}' if self.version else 'application/json'

        r = requests.request(method=http_method, url=config.BASE_URL + endpoint, params=params, headers=headers, data=data)
        
        try:
            return r.json()
        except requests.exceptions.JSONDecodeError as e:
            raise requests.exceptions.JSONDecodeError(f'Encountered status code {r.status_code}. See response below:\n{r.text}', e.doc, e.pos)
        
request_executor = RequestExecutor(config.VERSION)