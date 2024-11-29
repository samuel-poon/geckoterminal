from enum import Enum

class Timeframe(Enum):
    DAY     = 'DAY'
    HOUR    = 'HOUR'
    MINUTE  = 'MINUTE'

class TokenDenomination:
    BASE    = 'base'
    QUOTE   = 'quote'