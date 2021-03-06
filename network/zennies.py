
from clove.network.bitcoin import Bitcoin


class Zennies(Bitcoin):
    """
    Class with all the necessary ZENI network information based on
    http://www.github.com/zennies/zennies/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'zennies'
    symbols = ('ZENI', )
    nodes = ('54.214.213.181', '54.186.147.219', '91.134.120.210')
    port = 11011
    message_start = b'\x2a\x7c\xcb\xab'
    base58_prefixes = {
        'PUBKEY_ADDR': 80,
        'SCRIPT_ADDR': 72,
        'SECRET_KEY': 142
    }
