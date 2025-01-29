def count_divisors(n):
    """
    1 から n までの各整数の約数の個数を計算する
    """
    divisors = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j] += 1
    return divisors


# 入力
N = int(input())

# 約数の個数を事前計算
divisors = count_divisors(N)

# 答えを計算
total_count = 0
for X in range(1, N):
    Y = N - X
    total_count += divisors[X] * divisors[Y]

# 出力
print(total_count)
