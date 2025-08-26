# 入力
h, w, m = map(int, input().split())
t = []
a = []
x = []
for _ in range(m):
    ti, ai, xi = map(int, input().split())
    t.append(ti)
    a.append(ai - 1)  # 0-indexed に変換
    x.append(xi)

# 行・列の塗られたフラグ
row_done = [False] * h
col_done = [False] * w

# 未処理の行・列の数
hc = h
wc = w

# 色ごとの確定セル数
X = 200010
cnt = [0] * X

# 操作を逆順に処理
for i in range(m - 1, -1, -1):
    if t[i] == 1:
        if not row_done[a[i]]:
            row_done[a[i]] = True
            hc -= 1
            cnt[x[i]] += wc
    else:
        if not col_done[a[i]]:
            col_done[a[i]] = True
            wc -= 1
            cnt[x[i]] += hc

# 残った未塗りマス（色 0 と仮定）
cnt[0] += hc * wc

# 出力
ans = [(i, c) for i, c in enumerate(cnt) if c > 0]
print(len(ans))
for color, num in ans:
    print(color, num)
