# 入力
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# DPテーブルを作る：dp[i][j] = i枚目まで使って合計jを作れるかどうか
# 初期値はすべてFalse
dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][0] = True  # 0枚使って合計0は作れる（初期状態）

# DP配列の更新
for i in range(N):  # i = 0 から N-1 まで
    a, b = A[i]  # i番目のコインの表と裏の値
    for j in range(M + 1):  # 合計値をjとして試す
        if dp[i][j]:  # もし今の時点で合計jが作れているなら
            if j + a <= M:
                dp[i + 1][j + a] = True  # 表を使って合計が増える
            if j + b <= M:
                dp[i + 1][j + b] = True  # 裏を使って合計が増える

# 合計Mが作れなかった場合
if not dp[N][M]:
    print("No")
    exit()

# 復元処理：どのコインの表 or 裏を使ったかを調べる
num = M
res = []

# N枚目から逆順にたどる
for i in range(N - 1, -1, -1):
    a, b = A[i]
    # 表（H）を使った場合を調べる
    if num - a >= 0 and dp[i][num - a]:
        res.append("H")
        num -= a
    # 裏（T）を使った場合を調べる
    elif num - b >= 0 and dp[i][num - b]:
        res.append("T")
        num -= b

# 出力
res.reverse()  # 逆順にたどってきたので、正しい順に直す
print("Yes")
print("".join(res))
