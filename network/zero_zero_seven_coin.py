from clove.network.bitcoin import Bitcoin


class Coin007(Bitcoin):
    """
    Class with all the necessary  007Coin (007) network information based on
    https://github.com/007coindev/007coin/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = '007coin'
    symbols = ('007', )
    nodes = ('46.101.7.165', )
    port = 11007
    message_start = b'\x2f\x24\x15\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 63,
        'SECRET_KEY': 153
    }
