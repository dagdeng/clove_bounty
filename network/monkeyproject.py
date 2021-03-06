from clove.network.bitcoin import Bitcoin


class MonkeyProject(Bitcoin):
    """
    Class with all the necessary MonkeyProject network information based on
    https://github.com/monkeyproject/monkey/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'MonkeyProject'
    symbols = ('MONK', )
    nodes = ('185.150.191.36', '185.150.191.23', )
    port = 8710
    message_start = b'\x42\xa4\xc5\x2b'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 179
    }


# Has no testnet
