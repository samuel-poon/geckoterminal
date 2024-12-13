from .request_executor import request_executor

from typing import Iterable, Optional

def get_pool(
        network: str,
        pool_address: str,
        include: Iterable[str] = ['base_token', 'quote_token', 'dex']
    ):
    params = {
        'include':','.join(include)
    }

    return request_executor.request(f'/networks/{network}/pools/{pool_address}', params=params)

def get_pools(
        network: str,
        pool_addresses: Iterable[str],
        include: Iterable[str] = ['base_token', 'quote_token', 'dex']
    ):
    params = {
        'include':','.join(include)
    }

    return request_executor.request(f'/networks/{network}/pools/multi/{",".join(pool_addresses)}', params=params)

def get_trending_pools(
        network: Optional[str]  = None,
        include: Iterable[str]  = ['base_token', 'quote_token', 'dex'],
        page: int               = 1
    ):
    params = {
        'include':','.join(include),
        'page':page
    }

    endpoint = f'/networks/{network}/trending_pools' if network else f'/networks/trending_pools'

    return request_executor.request(endpoint, params=params)

def get_top_pools(
        network: str,
        dex: Optional[str]      = None,
        include: Iterable[str]  = ['base_token', 'quote_token', 'dex'],
        page: int               = 1
    ):
    params = {
        'include':','.join(include),
        'page':page
    }

    endpoint = f'/networks/{network}/dexes/{dex}/pools' if dex else f'/networks/{network}/pools'
    
    return request_executor.request(endpoint, params=params)

def get_new_pools(
        network: Optional[str]  = None,
        include: Iterable[str]  = ['base_token', 'quote_token', 'dex'],
        page: int               = 1
    ):
    """
    If network is not included, returns the latest 20 pools across all networks.
    """
    params = {
        'include':','.join(include),
        'page':page
    }

    return request_executor.request(f'/networks{"/" + network if network else ""}/new_pools', params=params)

def search_pools(
        query: str,
        network: Optional[str]  = None,
        include: Iterable[str]  = ['base_token', 'quote_token', 'dex'],
        page: int               = 1
    ):
    params = {
        'query':query,
        'network':network,
        'include':','.join(include),
        'page':page
    }

    return request_executor.request('/search/pools', params=params)