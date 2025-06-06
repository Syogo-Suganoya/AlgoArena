N, M = map(int, input().split())
A = list(map(int, input().split()))

# 最初の M 個をウィンドウとして保持
from collections import Counter

counter = Counter(A[:M])
res = len(counter)  # 現時点での異なる色の数

# ウィンドウをスライドさせて、最大の色数を求める
for i in range(M, N):
    # 左端を削除
    out_color = A[i - M]
    counter[out_color] -= 1
    if counter[out_color] == 0:
        del counter[out_color]

    # 新しい色を追加
    in_color = A[i]
    counter[in_color] += 1

    # 異なる色の数を更新
    res = max(res, len(counter))

# 答えを出力
print(res)
