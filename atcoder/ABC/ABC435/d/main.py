import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[y].append(x)

Q = int(input())

flags = [False] * N


def dfs(start):
    stack = [start]
    while stack:
        u = stack.pop()
        for nxt in graph[u]:
            if flags[nxt]:
                continue
            flags[nxt] = True
            stack.append(nxt)


for _ in range(Q):
    T, V = map(int, input().split())
    V -= 1
    match T:
        case 1:
            if flags[V]:
                continue
            flags[V] = True
            dfs(V)
        case 2:
            print("Yes" if flags[V] else "No")
