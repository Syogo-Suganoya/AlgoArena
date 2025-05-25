from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

t = sum(A)  # 配列Aの合計
res = float("inf")

# 0からN-1までのインデックスでループ
for i in range(N + 1):
    # Aの中から i 個選ぶすべての組み合わせを生成
    for c in combinations(A, i):
        ts = sum(c)  # 部分集合の合計
        tmp = max(ts, t - ts)  # 2つに分けた時の大きい方
        res = min(res, tmp)  # 最小値を更新

print(res)
