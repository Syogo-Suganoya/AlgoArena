import sys

sys.setrecursionlimit(10**6)  # 再帰の上限を引き上げ（Nが大きいので必須）

N = int(input())
A = list(map(int, input().split()))

# 子リストを作成（0番目は使わない）
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[A[i - 2]].append(i)

# 部分木サイズ格納用
subtree_size = [0] * (N + 1)


def dfs(u):
    size = 1  # 自分自身をカウント
    for v in G[u]:
        size += dfs(v)  # 子の部分木サイズを足す
    subtree_size[u] = size
    return size


dfs(1)

# 部下の数 = 部分木サイズ - 1
ans = [subtree_size[i] - 1 for i in range(1, N + 1)]
print(*ans)
