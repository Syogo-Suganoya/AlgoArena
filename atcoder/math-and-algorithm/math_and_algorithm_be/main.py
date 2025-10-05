import math
from itertools import combinations

N, K = map(int, input().split())
V = list(map(int, input().split()))

# 包除原理でカウント
count = 0
V_set = list(set(V))  # 重複除去
K = len(V_set)

for r in range(1, K + 1):
    for comb in combinations(V_set, r):
        # 組み合わせの LCM を計算
        L = 1
        for x in comb:
            L = math.lcm(L, x)
            if L > N:  # LCM が N を超えたら以降は不要
                break
        if L > N:
            continue
        # 奇数個なら加算、偶数個なら減算
        if r % 2 == 1:
            count += N // L
        else:
            count -= N // L

print(count)
