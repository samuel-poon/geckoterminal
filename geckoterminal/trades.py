from .request_executor import request_executor

def get_trades(
        network: str,
        pool_address: str,
        trade_volume_in_usd_greater_than: int | float = 0
    ):
    '''Returns last 300 trades in past 24 hours from pool.'''
    
    params = {
        'trade_volume_in_usd_greater_than':trade_volume_in_usd_greater_than
    }

    return request_executor.request(f'/networks/{network}/pools/{pool_address}/trades', params=params)