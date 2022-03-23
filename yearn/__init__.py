from brownie import network
from yearn.logs import setup_logging
from yearn.sentry import setup_sentry
from yearn.cache import reduce_cache

setup_logging()
setup_sentry()
if network.is_connected():
    from yearn.middleware.middleware import setup_middleware
    setup_middleware()

reduce_cache()
