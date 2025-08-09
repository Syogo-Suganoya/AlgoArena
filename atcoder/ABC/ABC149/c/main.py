import math

N = int(input())


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# N以上で最初に見つかる素数を探す
while True:
    if isprime(N):
        print(N)
        break
    N += 1
