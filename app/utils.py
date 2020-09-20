from functools import lru_cache

import sys
sys.setrecursionlimit(100000)


@lru_cache()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
