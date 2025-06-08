N, Q = map(int, input().split())

# imos配列の準備
c = [0] * (N + 2)  # 1-indexedにして扱いやすく（N+2必要）

# クエリ処理
for _ in range(Q):
    L, R, X = map(int, input().split())
    c[L] += X
    c[R + 1] -= X

# 累積和の計算
for i in range(1, N + 1):
    c[i] += c[i - 1]

# 結果の構築
res = []
for i in range(2, N + 1):
    if c[i - 1] < c[i]:
        res.append("<")
    elif c[i - 1] == c[i]:
        res.append("=")
    else:
        res.append(">")

print("".join(res))
