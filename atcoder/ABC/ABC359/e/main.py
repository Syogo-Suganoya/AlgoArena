N = int(input())
A = list(map(int, input().split()))

# 高さについて単調減少になるように (高さ, 個数) を管理する
rectangles = []

# 1 + ∑ 高さ × 個数
ans = 1
res = []

for a in A:
    count = 1  # 新しい高さは最初は個数1

    # H より低いものがある限り更新
    while rectangles and rectangles[-1][0] <= a:
        h, c = rectangles.pop()
        ans -= h * c  # 合計から h * c を引く
        count += c  # 個数を増やす

    # 合計に H * count を足す
    ans += a * count
    rectangles.append((a, count))
    res.append(ans)
print(*res)
