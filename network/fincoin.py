from clove.network.bitcoin import Bitcoin


class FinCoin(Bitcoin):
    """
    Class with all the necessary FinCoin (FNC) network information based on
    https://github.com/Fincoinltd/FNC/blob/master/fincoin-src/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'fincoin'
    symbols = ('FNC', )
    seeds = ('seed5.cryptolife.net', 'seed2.cryptolife.net', 'seed3.cryptolife.net',
             'electrum1.cryptolife.net', 'wallet.cryptolife.net', 'explore.cryptolife.net')
    port = 20092
    message_start = b'\xb4\xf8\xe2\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 163
    }

# no testnet
