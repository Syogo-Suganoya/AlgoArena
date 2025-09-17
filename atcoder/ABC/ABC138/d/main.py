import sys

sys.setrecursionlimit(1 << 25)  # 再帰深さは念のため大きめに
input = sys.stdin.readline

# 入力
N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1  # 0-indexed に
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# 差分配列
up = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    up[p] += x

ans = [0] * N  # 最終値

# スタック DFS で累積値を計算
stack = [(0, -1, 0)]  # (現在ノード, 親ノード, 親からの累積値)
while stack:
    u, parent, acc = stack.pop()
    total = acc + up[u]
    ans[u] = total
    for v in edges[u]:
        if v != parent:
            stack.append((v, u, total))

# 結果出力
print(*ans)
