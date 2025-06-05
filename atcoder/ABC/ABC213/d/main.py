import sys

sys.setrecursionlimit(300000)  # ★再帰制限を上げる

N = int(sys.stdin.readline())
G = [[] for _ in range(N + 1)]

# --- グラフ構築 ---
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

# --- 辞書順にする ---
for v in range(1, N + 1):
    G[v].sort()  # 小さい順に辿りたい

ans = []


def dfs(v: int, parent: int = -1) -> None:
    """辞書順 DFS（オイラーツアー）"""
    ans.append(v)  # 入るとき
    for nv in G[v]:
        if nv == parent:
            continue
        dfs(nv, v)
        ans.append(v)  # 戻るとき


dfs(1)
print(*ans)
