import pandas as pd

from .client import client
from . import config

def get_prices(network, token_addresses):
    return client.request(f'/simple/networks/{network}/token_price/{",".join(token_addresses)}')

def get_networks(page=1):
    params = {
        'page':page
    }

    return client.request('/networks', params=params)

def get_dexes(network, page=1):
    params = {
        'page':page
    }

    return client.request(f'/networks/{network}/dexes', params=params)

def get_pool(network, pool_address, include=['base_token', 'quote_token', 'dex']):
    params = {
        'include':','.join(include)
    }

    return client.request(f'/networks/{network}/pools/{pool_address}', params=params)

def get_pools(network, pool_addresses, include=['base_token', 'quote_token', 'dex']):
    params = {
        'include':','.join(include)
    }

    return client.request(f'/networks/{network}/pools/multi/{",".join(pool_addresses)}', params=params)

def get_trending_pools(network=None, include=['base_token', 'quote_token', 'dex'], page=1):
    params = {
        'include':','.join(include),
        'page':page
    }

    endpoint = f'/networks/{network}/trending_pools' if network else f'/networks/trending_pools'

    return client.request(endpoint, params=params)

def get_top_pools(network, dex=None, include=['base_token', 'quote_token', 'dex'], page=1):
    params = {
        'include':','.join(include),
        'page':page
    }

    endpoint = f'/networks/{network}/dexes/{dex}/pools' if dex else f'/networks/{network}/pools'
    
    return client.request(endpoint, params=params)

def get_new_pools(network=None, include=['base_token', 'quote_token', 'dex']):
    """
    If network is not included, returns the latest 20 pools across all networks.
    """
    params = {
        'include':','.join(include)
    }

    return client.request(f'/networks{"/" + network if network else ""}/new_pools', params=params)

def search_pools(query, network=None, include=['base_token', 'quote_token', 'dex'], page=1):
    params = {
        'query':query,
        'network':network,
        'include':','.join(include),
        'page':page
    }

    return client.request('/search/pools', params=params)

def get_token(network, token_address, include=['top_pools']):
    params = {
        'include':','.join(include)
    }
    
    return client.request(f'/networks/{network}/tokens/{token_address}', params=params)

def get_tokens(network, token_addresses, include=['top_pools']):
    params = {
        'include':','.join(include)
    }
    
    return client.request(f'/networks/{network}/tokens/multi/{",".join(token_addresses)}', params=params)

def get_top_pools_for_token(network, token_address, include=['base_token', 'quote_token', 'dex']):
    params = {
        'include':','.join(include)
    }

    return client.request(f'/networks/{network}/tokens/{token_address}/pools', params=params)

def get_token_info(network, token_address):
    return client.request(f'/networks/{network}/tokens/{token_address}/info')

def get_pool_info(network, pool_address):
    return client.request(f'/networks/{network}/pools/{pool_address}/info')

def get_pool_ohlcv(
        network,
        pool_address,
        timeframe='day',
        aggregate=1,
        before_timestamp=None,
        limit=None,
        currency='usd',
        token='base',
        df=False
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
        'token':token
    }

    response = client.request(f'/networks/{network}/pools/{pool_address}/ohlcv/{timeframe}', params=params)

    if df:
        try:
            ohlcv_list = response['data']['attributes']['ohlcv_list']
            return pd.DataFrame(ohlcv_list, columns=config.OHLCV_COLUMNS)
        except KeyError: # If the response does not have the expected structure
            raise ValueError(f'Could not parse OHLCV data into a DataFrame. See response below.\n\n{response}')

    return response

def get_trades(network, pool_address, trade_volume_in_usd_greater_than=0):
    # Returns last 300 trades in past 24 hours from pool
    
    params = {
        'trade_volume_in_usd_greater_than':trade_volume_in_usd_greater_than
    }

    return client.request(f'/networks/{network}/pools/{pool_address}/trades', params=params)
