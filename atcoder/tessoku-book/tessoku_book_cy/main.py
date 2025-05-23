import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
res = 0
for i in range(N + 1):
    if isprime(i):
        print(i)
