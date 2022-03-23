import os
from brownie import chain
from joblib import Memory

CACHE_SIZE = int(os.getenv("CACHE_SIZE", 1<<30)) # default to 1 GB
memory = Memory(f'cache/{chain.id}', verbose=0, bytes_limit=CACHE_SIZE)

def reduce_cache():
    memory.reduce_size()
