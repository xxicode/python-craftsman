from functools import lru_cache


@lru_cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


for i in range(0, 10):
    print(fib(i))

for i in range(0, 10):
    print(fib_loop(i))
