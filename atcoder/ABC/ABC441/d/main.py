import sys

sys.setrecursionlimit(10**7)

# 入力
n, m, L, S, T = map(int, input().split())

# グラフ
e = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    e[u - 1].append((v - 1, c))

# 到達可能フラグ
flag = [False] * n


def dfs(k, d, tot):
    """
    k   : 現在の頂点
    d   : これまでに使った辺の本数
    tot : 合計コスト
    """
    if d == L:
        if S <= tot <= T:
            flag[k] = True
        return

    if d < L:
        for nxt, cost in e[k]:
            dfs(nxt, d + 1, tot + cost)


# 始点 0 から探索
dfs(0, 0, 0)

# 答えを出力（1-indexed）
ans = []
for i in range(n):
    if flag[i]:
        ans.append(i + 1)

print(*ans)
