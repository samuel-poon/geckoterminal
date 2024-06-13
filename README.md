# GeckoTerminal

Python wrapper for GeckoTerminal's API. Access DEX data across >100 networks through an easy-to-use library.

## Installation
```
pip3 install geckoterminal
```

## GeckoTerminal Docs

https://www.geckoterminal.com/dex-api

## Quick Start
```python
import geckoterminal
```

### Get networks
```python
networks = geckoterminal.get_networks(page=1)
```

### Get prices
Supports up to 30 token addressses.
```python
prices = geckoterminal.get_prices(
    network='eth',
    token_addresses=[
        '0xdac17f958d2ee523a2206206994597c13d831ec7', # USDT
        '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', # USDC
        '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', # WETH
    ]    
)
```

### Get DEXes
```python
dexes = geckoterminal.get_dexes(
    network='eth',
    page=1
)
```

### Get pool
```python
weth_usdc = geckoterminal.get_pool(
    network='eth',
    pool_address='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640', # WETH/USDC Uniswap v3 0.05%
    include=['base_token', 'quote_token', 'dex']
)
```

### Get multiple pools
```python
solana_pools = geckoterminal.get_pools(
    network='solana',
    pool_addresses=[
        'FpCMFDFGYotvufJ7HrFHsWEiiQCGbkLCtwHiDnh7o28Q', # SOL/USDC Orca
        '3ne4mWqdYuNiYrYZC9TrA3FcfuFdErghH97vNPbjicr1', # BONK/SOL Orca
        'EP2ib6dYdEeqD8MfE2ezHCxX3kP3K2eLKkirfPm5eyMx', # $WIF/SOL Raydium
    ]
)
```

### Get top pools on a network
```python
polygon_top_pools = geckoterminal.get_top_pools(
    network='polygon_pos',
    include=['base_token', 'quote_token', 'dex']
)
```

### Get top pools on a DEX by network
```python
blaster_thruster_top_pools = geckoterminal.get_top_pools(
    network='blast',
    dex='thruster-v3', # Get id through geckoterminal.get_dexes(),
    include=['base_token', 'quote_token', 'dex']
)
```

### Get trades
```python
weth_usdc_trades = geckoterminal.get_trades(
    network='eth',
    pool_address='0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640', # WETH/USDC Uniswap v3 0.05%
    trade_volume_in_usd_greater_than=10000
)
```
