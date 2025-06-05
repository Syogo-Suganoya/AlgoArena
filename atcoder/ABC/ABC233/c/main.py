from collections import defaultdict

N, X = map(int, input().split())
l = []
for _ in range(N):
    A = list(map(int, input().split()))
    l.append(A[1:])  # A[0]は要素数なのでスキップ

# dp[i]: i個目まで選んで作れる積のパターン数を記録する辞書
dp = [defaultdict(int) for _ in range(N)]

# 最初の袋（0番目）について初期化
for a in l[0]:
    if a <= X:
        dp[0][a] += 1

# 各袋についてループ
for i in range(1, N):
    for val in l[i]:  # 現在の袋から1つ選ぶ
        for product in dp[i - 1]:  # 1つ前までの積の状態を参照
            new_product = product * val
            if new_product <= X:
                dp[i][new_product] += dp[i - 1][product]

# 最後の袋まで選んで、積がXになるパターン数を出力
print(dp[N - 1][X])
