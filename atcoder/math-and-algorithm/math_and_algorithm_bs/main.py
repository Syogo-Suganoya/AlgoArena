import math

N = int(input())
res = float("inf")

# i の範囲は 1 ～ (N // 2) + 1（1-indexedの意味合いも含めて）
for i in range(1, int(math.isqrt(N)) + 1):
    d, m = divmod(N, i)
    if m != 0:
        continue  # 割り切れない場合はスキップ

    # 処理コストの計算
    t = d * 2 + i * 2

    # 最小値を更新
    res = min(res, t)

print(res)
