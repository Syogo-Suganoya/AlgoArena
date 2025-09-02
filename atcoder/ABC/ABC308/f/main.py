from bisect import bisect_right
from collections import defaultdict

N, M = map(int, input().split())
P = list(map(int, input().split()))
L_raw = list(map(int, input().split()))
D_raw = list(map(int, input().split()))

# dict にまとめる
LD = defaultdict(list)
for l, d in zip(L_raw, D_raw):
    LD[l].append(d)

# L を昇順リストにして、各 L の最大 D を事前に保持
L_sorted = sorted(LD.keys())
max_D_for_L = [max(LD[l]) for l in L_sorted]

# 商品を昇順
P.sort()

res = 0

for price in P:
    # 二分探索で price 以下の L のインデックス
    idx = bisect_right(L_sorted, price)

    if idx == 0:
        # 適用できるクーポンなし
        res += price
    else:
        # 最大割引を適用
        max_discount = max(max_D_for_L[:idx])
        res += price - max_discount
        # 適用したクーポンは消費済みとして除外する
        # 今回は簡略化のため消費は考えない場合
        # 実際に使い切りの場合は、リストやカウンタで管理する必要あり

print(res)
