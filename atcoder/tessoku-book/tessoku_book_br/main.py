from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
ops = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

# 初期状態ビットマスク
start = 0
for i in range(N):
    if A[i]:
        start |= 1 << i

# 目標はすべてON： (1 << N) - 1
goal = (1 << N) - 1

# BFS 用
dist = [-1] * (1 << N)
dq = deque([start])
dist[start] = 0

while dq:
    s = dq.popleft()
    if s == goal:
        print(dist[s])
        break
    # 全操作を試す
    for x, y, z in ops:
        ns = s ^ (1 << x) ^ (1 << y) ^ (1 << z)
        if dist[ns] == -1:
            dist[ns] = dist[s] + 1
            dq.append(ns)
else:
    print(-1)  # もしONにできない場合
