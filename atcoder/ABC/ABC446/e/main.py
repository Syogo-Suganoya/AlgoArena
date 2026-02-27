from collections import deque

m, a, b = map(int, input().split())

# backward edges
edges = [[] for _ in range(m * m)]
for i in range(m):
    for j in range(m):
        k = (i * b + j * a) % m
        edges[j * m + k].append(i * m + j)

# bfs init
isseen = [0] * (m * m)
que = deque()
for i in range(m):
    for j in range(m):
        if i == 0 or j == 0:
            v = i * m + j
            isseen[v] = 1
            que.append(v)

# bfs run
while que:
    v = que.popleft()
    for u in edges[v]:
        if not isseen[u]:
            isseen[u] = 1
            que.append(u)

# count answers
ans = sum(1 for x in isseen if x == 0)
print(ans)
