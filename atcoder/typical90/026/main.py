from collections import deque

N = int(input())
T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    T[a].append(b)
    T[b].append(a)
que = deque([0])
visit = [-1 for _ in range(N)]  # 深さを管理
visit[0] = 0  # ノード0の深さは0
while que:  # BFS
    cur = que.popleft()
    for nxt in T[cur]:
        if visit[nxt] != -1:
            continue
        que.append(nxt)
        visit[nxt] = visit[cur] + 1

odd, even = [], []
for i in range(N):
    if visit[i] % 2 == 0:
        even.append(i + 1)
    else:
        odd.append(i + 1)
if len(even) > len(odd):
    print(*even[: N // 2])
else:
    print(*odd[: N // 2])
