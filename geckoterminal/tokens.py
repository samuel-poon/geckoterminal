from .request_executor import request_executor

from typing import Iterable, Optional

def get_token(
        network: str,
        token_address: str,
        include: Iterable[str] = ['top_pools']
    ):
    params = {
        'include':','.join(include)
    }
    
    return request_executor.request(f'/networks/{network}/tokens/{token_address}', params=params)

def get_tokens(
        network: str,
        token_addresses: Iterable[str],
        include: Iterable[str]          = ['top_pools']
    ):
    params = {
        'include':','.join(include)
    }
    
    return request_executor.request(f'/networks/{network}/tokens/multi/{",".join(token_addresses)}', params=params)

def get_top_pools_for_token(
        network: str,
        token_address: str,
        include: Iterable[str] = ['base_token', 'quote_token', 'dex']
    ):
    params = {
        'include':','.join(include)
    }

    return request_executor.request(f'/networks/{network}/tokens/{token_address}/pools', params=params)

def get_token_info(
        network: str,
        token_address: str
    ):
    return request_executor.request(f'/networks/{network}/tokens/{token_address}/info')

def get_pool_info(
        network: str,
        pool_address: str
    ):
    return request_executor.request(f'/networks/{network}/pools/{pool_address}/info')

def get_recently_updated_tokens_info(
        network: Optional[str] = None,
        include: Iterable[str] = ['include'],
    ):

    params = {
        'network': network,
        'include': ','.join(include)
    }

    return request_executor.request('/tokens/info_recently_updated', params=params)