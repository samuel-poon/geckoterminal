# GeckoTerminal

Python wrapper for GeckoTerminal's API.

## Installation
```
pip3 install git+https://github.com/samuel-poon/geckoterminal.git
```

## GeckoTerminal Docs

https://www.geckoterminal.com/dex-api

## Quick Start
```python
import geckoterminal

networks = geckoterminal.get_networks()
dexes = geckoterminal.get_dexes(network='eth')
weth_usdc = geckoterminal.get_pool(network='eth', pool_address='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640')
polygon_top_pools = geckoterminal.get_top_pools(network='polygon_pos')
```
