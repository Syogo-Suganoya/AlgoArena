from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

dis = [-1] * N
Q = int(input())

for _ in range(Q):
    x, k = map(int, input().split())
    x -= 1
    q = deque([x])
    dis[x] = 0
    vs = []

    while q:
        u = q.popleft()
        vs.append(u)
        if dis[u] == k:
            continue
        for v in E[u]:
            if dis[v] != -1:
                continue
            dis[v] = dis[u] + 1
            q.append(v)

    ans = 0
    for v in vs:
        ans += v + 1
        dis[v] = -1  # リセット
    print(ans)
