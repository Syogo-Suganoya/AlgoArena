N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

res = 0
for i, index in enumerate(graph):
    if len(list(filter(lambda x: i + 1 > x, index))) == 1:
        res += 1

print(res)
