import pandas as pd

from .request_executor import request_executor
from .enums import Timeframe, TokenDenomination
from . import config

from typing import Optional

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