N, M = map(int, input().split())
graph = [[False] * N for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A][B] = True
    graph[B][A] = True

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if graph[i][j] and graph[j][k] and graph[k][i]:
                ans += 1
print(ans)
