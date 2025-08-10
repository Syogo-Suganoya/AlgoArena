from collections import Counter

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

# 正解者のカウント
counter = Counter(A)

threshold = Q - K + 1  # 参加賞のための正解回数の基準

for i in range(1, N + 1):
    if counter[i] >= threshold:
        print("Yes")
    else:
        print("No")
