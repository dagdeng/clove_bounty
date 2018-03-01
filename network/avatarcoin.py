from clove.network.bitcoin import Bitcoin


class AvatarCoin(Bitcoin):
    """
    Class with all the necessary AvatarCoin network information based on
    https://github.com/avatarcoin/avatarcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'AvatarCoin'
    symbols = ('AV', )
    seeds = ('avatar.altnodes.xyz', 'avatar2.altnodes.xyz')
    port = 9712


# Has no Testnet
