import os
from brownie import chain
from joblib import Memory

CACHE_SIZE = os.getenv("CACHE_SIZE", '100M') # default to 100 MB
memory = Memory(f'cache/{chain.id}', verbose=0, bytes_limit=CACHE_SIZE)

def reduce_cache():
    memory.reduce_size()
