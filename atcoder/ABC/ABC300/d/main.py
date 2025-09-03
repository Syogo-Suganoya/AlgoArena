N = int(input())


# エラトステネスの篩で素数を列挙する関数
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]  # 0と1は素数ではない
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes


# メイン処理
# 素数列挙の上限は √N 程度で十分
limit = int(N**0.5) + 1
primes = sieve(limit)

# 素数かどうかのフラグと、累積和のための配列
prefix_sum = [0] * (limit + 1)
is_prime = [False] * (limit + 1)
for p in primes:
    is_prime[p] = True

# 素数の個数の累積和を計算（高速に個数を引けるように）
for i in range(1, limit + 1):
    prefix_sum[i] = prefix_sum[i - 1] + (1 if is_prime[i] else 0)

ans = 0
# a < b < c を全探索。ただし制限を加えて高速化
for i in range(len(primes)):
    a = primes[i]
    if a**5 > N:
        break  # a^2 * b * c^2 >= a^5 なので、ここを超えたら打ち切り

    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a**2 * b**3 > N:
            break  # a^2 * b * c^2 >= a^2 * b^3 なのでここで打ち切り

        # 条件 a^2 * b * c^2 <= N より、cの上限を求める
        max_c = int((N / (a**2 * b)) ** 0.5)

        if b >= max_c:
            break  # b < c の条件に反する

        # 素数 c の候補数 = max_c 以下の素数の個数 - b 以下の素数の個数
        count_c = prefix_sum[max_c] - prefix_sum[b]
        ans += count_c

print(ans)
