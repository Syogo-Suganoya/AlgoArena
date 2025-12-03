import sys

# 再帰の上限を増やす（グラフの深さが深い場合に必要）
sys.setrecursionlimit(300000)


N, M = map(int, input().split())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append(y)

# dp[u]: 町uから到達可能な地点（u自身を含む）における金の最高価格
# 未計算の場合は -1 とする（価格は正なので識別可能）
dp = [-1] * N


def get_max_price(u):
    if dp[u] != -1:
        return dp[u]

    # 初期値は自分自身の価格
    res = A[u]

    # 子ノード（行き先の町）を探索
    for v in adj[u]:
        # 子ノード以降の最大値と比較して更新
        res = max(res, get_max_price(v))

    dp[u] = res
    return res


ans = -float("inf")

# 全ての町を買う場所の候補として走査
for i in range(N):
    # 行き先がない町では買っても売れないのでスキップ
    if not adj[i]:
        continue

    # 町 i で買った場合、隣接する町 v 以降の最大価格で売るのが最適
    # (直接 v で売るか、v のさらに先で売るかは get_max_price(v) が解決済み)
    max_sell_price = -float("inf")
    for v in adj[i]:
        max_sell_price = max(max_sell_price, get_max_price(v))

    # 利益計算
    profit = max_sell_price - A[i]

    if profit > ans:
        ans = profit

print(ans)
