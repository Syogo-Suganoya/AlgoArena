N, X, Y = map(int, input().split())

X -= 1
Y -= 1

ans = [0] * N

# i < j のすべてのペアを調べる
for i in range(N):
    for j in range(i + 1, N):
        # 直線だけの場合
        d1 = j - i
        # X-Y の枝を使う場合（i→X→Y→j）
        d2 = abs(i - X) + 1 + abs(Y - j)
        # 逆に（i→Y→X→j）
        d3 = abs(i - Y) + 1 + abs(X - j)
        d = min(d1, d2, d3)
        ans[d] += 1

# 1 から N-1 の距離ごとに出力
for k in range(1, N):
    print(ans[k])
