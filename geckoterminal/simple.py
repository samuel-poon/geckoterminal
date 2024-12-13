from .request_executor import request_executor

def get_prices(
        network: str,
        token_addresses: str
    ):
    return request_executor.request(f'/simple/networks/{network}/token_price/{",".join(token_addresses)}')