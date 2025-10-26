# 入力
n, m, c = map(int, input().split())
a = list(map(int, input().split()))

# 配列をソート
a.sort()

# 種類ごとの値
b = []
# その出現回数
p = []
idx = 0

while idx < n:
    b.append(a[idx])
    nxt = idx + 1
    while nxt < n and a[nxt] == a[idx]:
        nxt += 1
    p.append(nxt - idx)  # 同じ値の出現回数
    idx = nxt

k = len(b)  # 値の種類数

r = 0  # 右端ポインタ
cur = 0  # 現在のカウント（累積）
ans = 0  # 答え

for i in range(k):
    # cur が c 以上になるまで右に伸ばす
    while cur < c:
        cur += p[r]
        r += 1
        if r >= k:
            r -= k  # 循環させる

    # 答えの更新
    if i == 0:
        ans += (m + b[0] - b[k - 1]) * cur  # 最初の区間は特殊処理
    else:
        ans += (b[i] - b[i - 1]) * cur

    # 左端を減らす
    cur -= p[i]

print(ans)
