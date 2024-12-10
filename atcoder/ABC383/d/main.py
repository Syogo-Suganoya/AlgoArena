from sympy import primerange


def count_numbers_with_9_divisors(N):
    primes = list(primerange(int(N**0.5)))
    count = 0
    # Case 1: p^8
    for p in primes:
        if p**8 <= N:
            count += 1
        else:
            break
    # Case 2: p^2 * q^2
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] ** 2 * primes[j] ** 2 <= N:
                count += 1
            else:
                break
    return count


# 入力
N = int(input())
# 計算と出力
result = count_numbers_with_9_divisors(N)
print(result)
