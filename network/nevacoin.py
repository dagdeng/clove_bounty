
from clove.network.bitcoin import Bitcoin


class NevaCoin(Bitcoin):
    """
    Class with all the necessary NEVA network information based on
    http://www.github.com/Nevacoin/nevacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'nevacoin'
    symbols = ('NEVA', )
    seeds = ('n1.nevacoin.net', 'n2.nevacoin.net',
             'n3.nevacoin.net', 'n4.nevacoin.net', 'seed.crypto.si')
    port = 7391


class NevaCoinTestNet(NevaCoin):
    """
    Class with all the necessary NEVA testing network information based on
    http://www.github.com/Nevacoin/nevacoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-nevacoin'
    seeds = (
        'node.bit-coin.pw', 'krile.bit-coin.pw', 'neva-seed01.chainworksindustries.com',
        'neva-seed02.chainworksindustries.com', 'neva-seed03.chainworksindustries.com',
        'neva-seed04.chainworksindustries.com', 'neva-seed05.chainworksindustries.com',
        'test1.nevacoin.pw'
    )
    port = 17391
