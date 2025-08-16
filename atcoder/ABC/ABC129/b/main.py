N = int(input())
W = list(map(int, input().split()))

total = sum(W)  # 全部の重りの合計
prefix = 0  # 左側の合計（最初は0）
ans = total  # 最小差。とりあえず大きい値から始める

# 前から順に、区切る場所を動かしていく
for i in range(N - 1):  # 最後で分けるのはできないから N-1 まで
    prefix += W[i]  # 左に1個追加
    right = total - prefix  # 残りは右
    diff = abs(prefix - right)  # 差の絶対値
    ans = min(ans, diff)  # 今までの最小と比べて更新

print(ans)
