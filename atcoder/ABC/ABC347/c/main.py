N, A, B = map(int, input().split())
D = list(map(int, input().split()))

# 予定を週の中の位置に変換（周期問題）
# A+B日で1周期なので、余りを計算すると週の何日目かになる
X = []
for i in range(N):
    v = D[i] % (A + B)
    X.append(v)

# 週の中で予定がどこにあるかを昇順で並べる
X.sort()

# 隣接する予定の間隔を計算
Y = []
for i in range(N - 1):
    Y.append(X[i + 1] - X[i])  # 隣同士の差分

# 週をまたぐ場合の間隔も考慮
Y.append((A + B) - (X[-1] - X[0]))

# 間隔がB日以上あるかをチェック
# B日以上あれば、休日を確保できるので「Yes」
if max(Y) > B:
    print("Yes")
else:
    print("No")
