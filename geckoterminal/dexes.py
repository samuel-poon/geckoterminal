from .request_executor import request_executor

def get_dexes(
        network: str,
        page: int = 1
    ):
    params = {
        'page':page
    }

    return request_executor.request(f'/networks/{network}/dexes', params=params)