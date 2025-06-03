N = int(input())

# 素数判定のためのエラトステネスの篩
LIMIT = int(N ** (1 / 3)) + 10  # q の上限は立方根まで
is_prime = [True] * (LIMIT)
is_prime[0] = is_prime[1] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT, i):
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]

# 結果をカウントする
count = 0
for i in range(1, len(primes)):
    q = primes[i]
    q3 = q**3
    if q3 > N:
        break
    # p < q かつ p * q^3 <= N なので、p <= N // q^3
    max_p = N // q3
    for j in range(i):
        p = primes[j]
        if p <= max_p:
            count += 1
        else:
            break

print(count)
