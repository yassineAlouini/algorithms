# Generate a random Fibonacci number between two integers (min_n, max_n)

import numpy as np

np.random.seed(314)


def cache(func):
    c = {}

    def inner(n):
        if n in c:
            return c[n]
        else:
            c[n] = func(n)
            return c[n]
    return inner


@cache
def fib(n):
    assert n >= 0, 'n should be bigger than 0'
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@cache
def is_fib(n):
    i = 1
    while fib(i) <= n:
        if fib(i) == n:
            return True
        i += 1
    return False


def random_fib(min_n, max_n):
    n = np.random.randint(min_n, max_n + 1)
    while not is_fib(n):
        n = np.random.randint(min_n, max_n + 1)
    return n

if __name__ == "__main__":
    assert random_fib(1, 1) == 1
    assert random_fib(10, 13) == 13
    print(random_fib(20, 30))
