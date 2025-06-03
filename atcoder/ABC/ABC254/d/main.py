from collections import defaultdict

N = int(input())


# 各数を平方因子で割り切れるだけ割って、最小の形にする
def reduce_square_factors(n):
    res = 1
    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        # 奇数回のときのみ掛ける（偶数回だと平方因子）
        if cnt % 2 == 1:
            res *= i
        i += 1
    if n > 1:
        res *= n
    return res


# key: √(i×j) を構成する共通の因子、value: 出現数
count = defaultdict(int)

# 各数値の平方因子を取り除いた形を数える
for i in range(1, N + 1):
    key = reduce_square_factors(i)
    count[key] += 1

# 出現数に対して nC2 を計算（i × j が平方数になる条件）
ans = 0
for v in count.values():
    ans += v * v  # (i, j) で i × j が平方になる全通り

print(ans)
