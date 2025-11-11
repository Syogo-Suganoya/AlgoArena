N, M = map(int, input().split())
X = list(map(int, input().split()))

# 家の位置をソート
X.sort()

# M >= N の場合、全て別々に置けるので強度合計は 0
if M >= N:
    print(0)
    exit()

# 隣り合う家の距離を求める
diffs = [X[i + 1] - X[i] for i in range(N - 1)]

# 大きい間隔から M-1 個切り離す
diffs.sort(reverse=True)

# 残りの距離を合計する
ans = sum(diffs[M - 1 :])

print(ans)
