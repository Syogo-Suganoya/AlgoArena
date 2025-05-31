import bisect

N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# a_i の昇順にソート
AB.sort()

# a_i のリストと b_i の累積和を作成
A = [a for a, b in AB]
B = [b for a, b in AB]
cumB = [0]
for b in B:
    cumB.append(cumB[-1] + b)

# 二分探索
left = 0
right = max(A) + 2  # 上限を設定

while left < right:
    mid = (left + right) // 2
    # mid 日目までに飲む薬の総数を計算
    idx = bisect.bisect_right(A, mid)
    total = cumB[-1] - cumB[idx]
    if total <= K:
        right = mid
    else:
        left = mid + 1

print(left + 1)
