from clove.network.bitcoin import Bitcoin


class Digigems(Bitcoin):
    """
    Class with all the necessary Digigems network information based on
    https://github.com/jarno83/digigems/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'digigems'
    symbols = ('DGMS', )
    nodes = ("54.69.225.67", )
    port = 5333
    message_start = b'\xff\xc2\xb8\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 158
    }


class DigigemsTestNet(Digigems):
    """
    Class with all the necessary Digigems testing network information based on
    https://github.com/jarno83/digigems/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-digigems'
    nodes = ("88.196.13.22", )
    port = 15333
    message_start = b'\xac\xb1\xc7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
