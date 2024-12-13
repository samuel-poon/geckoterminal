from .request_executor import request_executor

def get_networks(
        page: int = 1
    ):
    params = {
        'page':page
    }

    return request_executor.request('/networks', params=params)