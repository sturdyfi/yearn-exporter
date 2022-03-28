
import pytest
import os
from brownie import chain, network
from yearn.networks import Network

network.connect(os.environ.get('BROWNIE_NETWORK_ID_MAINNET','mainnet'))

# Import must occur after brownie is connected.
from yearn.middleware.middleware import setup_middleware
setup_middleware()

mainnet_only = pytest.mark.skipif(
    chain.id != Network.Mainnet, reason="This test is only applicable on mainnet"
)
