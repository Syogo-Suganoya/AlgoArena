from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

# グラフ構築（有向）
for _ in range(M):
    a, b, w = map(int, input().split())
    G[a].append((b, w))

# dist[v][x] = 頂点vにXOR値xで到達できるか
MAX_XOR = 1024  # 10bitの範囲で十分（0〜1023）
visited = [[False] * MAX_XOR for _ in range(N + 1)]

# 初期状態：頂点1にいてXOR値0
dq = deque()
dq.append((1, 0))
visited[1][0] = True

while dq:
    v, val = dq.popleft()

    # すべての出辺を辿る
    for nv, w in G[v]:
        nxt = val ^ w  # 次のXOR値
        if not visited[nv][nxt]:
            visited[nv][nxt] = True
            dq.append((nv, nxt))

# 頂点Nに到達可能な最小のXOR値を探す
ans = -1
for x in range(MAX_XOR):
    if visited[N][x]:
        ans = x
        break

print(ans)
