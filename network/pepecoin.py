
from clove.network.bitcoin import Bitcoin


class PepeCoin(Bitcoin):
    """
    Class with all the necessary MEME network information based on
    http://www.github.com/pepeteam/pepecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'pepecoin'
    symbols = ('MEME', )
    seeds = ('seed.kekdaq.com', 'seed.pepecoin.co', )
    port = 29377
    message_start = b'\x3a\xc4\x2c\x2f'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }
