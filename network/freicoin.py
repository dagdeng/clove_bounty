from clove.network.bitcoin import Bitcoin


class Freicoin(Bitcoin):
    """
    Class with all the necessary Freicoin (FRC) network information based on
    https://github.com/freicoin/freicoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'freicoin'
    symbols = ('FRC', )
    seeds = ('seed.freico.in', 'fledge.freico.in',
             'seed.mainnet.freicoin.pw', 'dnsseed.sicanet.net')
    port = 8639
    message_start = b'\x2c\xfe\x7e\x6d'
    base58_prefixes = {
        'PUBKEY_ADDR': 0,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class FreicoinTestNet(Freicoin):
    """
    Class with all the necessary Freicoin (FRC) testing network information based on
    https://github.com/freicoin/freicoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-freicoin'
    seeds = ('seed.testnet.freicoin.pw', )
    port = 18639
    message_start = b'\x5e\xd6\x7c\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
