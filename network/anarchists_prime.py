from clove.network.bitcoin import Bitcoin


class AnarchistsPrime(Bitcoin):
    """
    Class with all the necessary  AnarchistsPrime (ACP) network information based on
    https://github.com/AnarchistsPrime/Acp2/tree/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'anarchistsprime'
    symbols = ('ACP', )
    seeds = ('acp.servep2p.com', )
    port = 11050
    message_start = b'\xf9\xbe\xb4\xd9'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }
