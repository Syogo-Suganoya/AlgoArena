N, K, M = map(int, input().split())
A = list(map(int, input().split()))

# 目標となる合計（平均 M を達成するために必要な合計）
target_sum = N * M

# すでにある合計
current_sum = sum(A)

# 足りない分
need = target_sum - current_sum

# K 以下ならそのまま出力、無理なら -1
if need <= K:
    print(max(0, need))
else:
    print(-1)
