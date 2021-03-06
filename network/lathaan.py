from clove.network.bitcoin import Bitcoin


class LAthaan(Bitcoin):
    """
    Class with all the necessary LAthaan network information based on
    https://github.com/Lathaan/Lathaan/blob/master/Lathaan/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'lathaan'
    symbols = ('LTH', )
    nodes = ("173.254.204.117", )
    port = 14987
    message_start = b'\xb3\xa2\x48\x6f'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 66,
        'SECRET_KEY': 161
    }

# no testnet
