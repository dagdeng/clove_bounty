from clove.network.bitcoin import Bitcoin


class MediumProject(Bitcoin):
    """
    Class with all the necessary MediumProject network information based on
    https://github.com/MEDIUMPROJECT/MEDIUM/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mediumproject'
    symbols = ('MPRO', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net",
             "wallet.cryptolife.net",
             "explore.cryptolife.net")
    port = 42815
