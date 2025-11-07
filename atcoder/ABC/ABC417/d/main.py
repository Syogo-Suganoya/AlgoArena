import bisect
from itertools import accumulate

# --- 入力 ---
N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
# 各プレゼントは (P_i, A_i, B_i)

# --- 最大テンションの上限 ---
# j + A_i がこの範囲を超えることはないので、
# DP配列のサイズをこの最大値に設定する
M = max(p + a for p, a, b in P)

# --- DPテーブルを初期化 ---
# dp[i][j]:
# 「i 番目以降のプレゼントを受け取ったとき」
# 現在のテンションが j の場合の、最終的なテンション値
dp = [[0] * (M + 1) for _ in range(N + 1)]

# すべてのプレゼントを受け取り終えたときは、テンション値 = そのまま j
for j in range(M + 1):
    dp[N][j] = j

# --- 後ろから前に向かってDPを構築 ---
# プレゼントを逆順に見て、「今のテンション j」から次にどう変化するかを求める
for i in range(N - 1, -1, -1):
    p, a, b = P[i]
    for j in range(M + 1):
        if j <= p:
            # テンションが閾値以下なら上昇（+A_i）
            # Mを超えないように min(M, j + a) でクリップ
            dp[i][j] = dp[i + 1][min(M, j + a)]
        else:
            # テンションが閾値を超えるなら減少（-min(j, B_i)）
            dp[i][j] = dp[i + 1][j - min(j, b)]

# --- B の累積和 ---
# 初期テンションが大きすぎるとき、いくつプレゼントを経ると範囲内に入るかを知るための前計算
sum_B = list(accumulate(b for _, _, b in P))


def access(x: int) -> int:
    """
    初期テンション x からスタートした場合の最終テンションを返す関数
    """
    # もしテンションがすでに範囲内なら、そのままDP表を参照
    if x <= M:
        return dp[0][x]

    # テンションが上限を超える場合：
    # 「どのタイミングで範囲内まで下がるか」を探す
    # x - M の分だけテンションを落とす必要がある
    idx = bisect.bisect_left(sum_B, x - M)

    if idx == len(sum_B):
        # すべてのプレゼントを受け取ってもまだ範囲外なら
        # 単純に累積B分だけ下がる
        return x - sum_B[-1]

    # 範囲内に入ったタイミングで、そこ以降のDP結果を参照
    # idx + 1 は「そのプレゼントの次」から再開することを意味する
    down_val = sum_B[idx]
    return dp[idx + 1][x - min(x, down_val)]


# --- クエリ処理 ---
Q = int(input())
for _ in range(Q):
    x = int(input())
    print(access(x))
