import pandas as pd

from typing import Iterable, Optional, Union

from .request_executor import request_executor
from .enums import Timeframe, TokenDenomination
from . import config

def get_prices(
        network: str,
        token_addresses: str
    ):
    return request_executor.request(f'/simple/networks/{network}/token_price/{",".join(token_addresses)}')

def get_networks(
        page: int = 1
    ):
    params = {
        'page':page
    }

    return request_executor.request('/networks', params=params)

def get_dexes(
        network: str,
        page: int = 1
    ):
    params = {
        'page':page
    }

    return request_executor.request(f'/networks/{network}/dexes', params=params)

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
        include: Iterable[str]  = ['base_token', 'quote_token', 'dex']
    ):
    """
    If network is not included, returns the latest 20 pools across all networks.
    """
    params = {
        'include':','.join(include)
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
        include: Iterable[str] = ['top_pools']
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

def get_pool_ohlcv(
        network: str,
        pool_address: str,
        timeframe: Timeframe            = Timeframe.DAY,
        aggregate: int                  = 1,
        before_timestamp: Optional[int] = None,
        limit: Optional[int]            = None,
        currency: str                   = 'usd',
        token: TokenDenomination        = TokenDenomination.BASE,
        df: bool                        = False
    ):
    """
    aggregate available values by timeframe:
      * day: 1
      * hour: 1, 4, 12
      * minute: 1, 5, 15
    """

    params = {
        'aggregate':aggregate,
        'before_timestamp':before_timestamp,
        'limit':limit,
        'currency':currency,
        'token':token.value if isinstance(token, TokenDenomination) else token
    }

    response = request_executor.request(f'/networks/{network}/pools/{pool_address}/ohlcv/{timeframe.value}', params=params)

    if df:
        try:
            ohlcv_list = response['data']['attributes']['ohlcv_list']
            return pd.DataFrame(ohlcv_list, columns=config.OHLCV_COLUMNS)
        except KeyError: # If the response does not have the expected structure
            raise ValueError(f'Could not parse OHLCV data into a DataFrame. See response below.\n\n{response}')

    return response

def get_trades(
        network: str,
        pool_address: str,
        trade_volume_in_usd_greater_than: Union[int, float] = 0):
    '''
    Returns last 300 trades in past 24 hours from pool.
    '''
    
    params = {
        'trade_volume_in_usd_greater_than':trade_volume_in_usd_greater_than
    }

    return request_executor.request(f'/networks/{network}/pools/{pool_address}/trades', params=params)
