from clove.network.bitcoin import Bitcoin


class Diamond(Bitcoin):
    """
    Class with all the necessary Diamond network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'diamond'
    symbols = ('DMD', )
    seeds = ("dnsseed.bit.diamonds", "37.120.186.85",
             "185.194.140.60", "188.68.39.1", "188.68.52.172")
    port = 17771
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }


class DiamondTestNet(Diamond):
    """
    Class with all the necessary Diamond testing network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-diamond'
    seeds = ("dnsseed.bit.diamonds")
    port = 51474
    message_start = b'\x45\x76\x65\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 139,
        'SCRIPT_ADDR': 19,
        'SECRET_KEY': 239
    }
