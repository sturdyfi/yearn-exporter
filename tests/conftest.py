
import pytest
from brownie import chain, network
from yearn.networks import Network

network.connect('mainnet')

mainnet_only = pytest.mark.skipif(
    chain.id != Network.Mainnet, reason="This test is only applicable on mainnet"
)
