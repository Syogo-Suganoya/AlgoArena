from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))

# SortedListを作成
sl = SortedList(A)

for _ in range(M):
    # 最大値を取得
    max_val = sl[-1]
    sl.pop(-1)  # 最大値を削除

    # 半額にする（切り捨て）
    half_val = max_val // 2

    # 半額にした値を挿入
    sl.add(half_val)

# 合計を出力
print(sum(sl))
