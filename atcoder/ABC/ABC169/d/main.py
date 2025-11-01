import math


# N を素因数分解して、各素因数の指数（何回割れるか）を求める関数
def factorization(n):
    factors = []
    for i in range(2, int(math.isqrt(n)) + 1):  # √n までで充分
        count = 0
        while n % i == 0:  # i で割れる間は割り続ける
            n //= i
            count += 1
        if count > 0:
            factors.append(count)  # i の指数を追加
    if n > 1:
        factors.append(1)  # n 自身が素数だった場合
    return factors


N = int(input())

exponents = factorization(N)  # 素因数の指数のリストを取得
total = 0

# 各指数に対して、その指数までに分割できる最大操作数を計算
for e in exponents:
    k = 1
    # 1 + 2 + ... + k ≤ e となる最大の k を探す（総和は k(k+1)//2）
    while k * (k + 1) // 2 <= e:
        k += 1
    total += k - 1  # 条件を超えたところで抜けるから1引く
print(total)
