n, m = map(int, input().split())

x = list(map(int, input().split()))
x = [xi - 1 for xi in x]

# 差分配列 v（長さ n+1）を初期化
v = [0] * (n + 1)


# 環状の距離を計算する関数
def dist(frm, to):
    """
    島 frm から島 to までの時計回りの距離を返す
    環状なので frm > to の場合は n を足す
    """
    if frm <= to:
        return to - frm
    else:
        return to + n - frm


# 差分配列に値を加算する関数
def add(frm, to, num):
    """
    差分配列 v に区間加算
    環状配列なので frm > to の場合は 2 つの区間に分ける
    """
    if frm <= to:
        v[frm] += num
        v[to] -= num
    else:
        v[frm] += num
        v[n] -= num
        v[0] += num
        v[to] -= num


# 移動順を順に見て、各橋の影響を差分配列に加算
for i in range(m - 1):
    # i 番目から i+1 番目への移動の距離を加算
    add(x[i], x[i + 1], dist(x[i + 1], x[i]))
    # i+1 番目から i 番目への移動の距離も加算（環状処理用）
    add(x[i + 1], x[i], dist(x[i], x[i + 1]))

# 累積和を取って各位置での最小距離を計算
ans = float("inf")
for i in range(n):
    v[i + 1] += v[i]  # 累積和
    ans = min(ans, v[i])  # 最小値を更新

# 結果を出力
print(ans)
