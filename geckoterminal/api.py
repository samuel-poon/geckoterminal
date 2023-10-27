import pandas as pd

from .client import client
from . import config

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

def get_top_pools(network, dex=None, include=['base_token', 'quote_token', 'dex']):
    params = {
        'include':','.join(include)
    }

    if dex:
        return client.request(f'/networks/{network}/dexes/{dex}/pools', params=params)
    else:
        return client.request(f'/networks/{network}/pools', params=params)

def get_new_pools(network=None, include=['base_token', 'quote_token', 'dex']):
    """
    If network is not included, returns the latest 20 pools across all networks.
    """
    params = {
        'include':','.join(include)
    }

    return client.request(f'/networks{"/" + network if network else ""}/new_pools', params=params)

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
        ohlcv_list = response['data']['attributes']['ohlcv_list']
        return pd.DataFrame(ohlcv_list, columns=config.OHLCV_COLUMNS)

    return response