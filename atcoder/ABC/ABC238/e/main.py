from collections import deque

# N: 配列の長さ, Q: クエリ数
N, Q = map(int, input().split())

# グラフを隣接リストで管理する
# 頂点は 0 ~ N （prefix sum S_0 ... S_N に対応）
edges = [[] for _ in range(N + 1)]

# クエリごとに辺を追加
# 区間 [l, r] の和が 0 という制約は S_{l-1} = S_r に対応する
# よって l-1 と r を辺で結ぶ
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    edges[l].append(r)
    edges[r].append(l)

# BFS（幅優先探索）で 0 から N に到達できるかを調べる
visited = [False] * (N + 1)
dq = deque([0])  # 始点は 0（S_0 = 0）
visited[0] = True

while dq:
    u = dq.popleft()
    for v in edges[u]:
        if not visited[v]:
            visited[v] = True
            dq.append(v)

# S_N が S_0 と同じ連結成分に含まれていれば、
# 全体の和が一意に 0 に決まる → Yes
# そうでなければ不定 → No
print("Yes" if visited[N] else "No")
