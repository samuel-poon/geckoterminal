# GeckoTerminal

Python wrapper for GeckoTerminal's API.

## Installation
```
pip3 install geckoterminal
```

## GeckoTerminal Docs

https://www.geckoterminal.com/dex-api

## Quick Start
```python
import geckoterminal

networks = geckoterminal.get_networks()
dexes = geckoterminal.get_dexes(network='eth')
weth_usdc = geckoterminal.get_pool(network='eth', pool_address='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640') # WETH/USDC Uniswap v3 0.05%
polygon_top_pools = geckoterminal.get_top_pools(network='polygon_pos')
weth_usdc_trades = geckoterminal.get_trades(
    network='eth',
    pool_address='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640',
    trade_volume_in_usd_greater_than=10000
)
```
