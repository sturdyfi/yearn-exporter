
import pytest
import os
from brownie import chain, network
from yearn.networks import Network

network.connect(os.environ.get('BROWNIE_NETWORK_ID_MAINNET','mainnet'))

mainnet_only = pytest.mark.skipif(
    chain.id != Network.Mainnet, reason="This test is only applicable on mainnet"
)
