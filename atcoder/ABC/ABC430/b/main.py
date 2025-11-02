N, M = map(int, input().split())
maze = [input() for _ in range(N)]

patterns = set()

for i in range(N - M + 1):
    for j in range(N - M + 1):
        subgrid = tuple(maze[x][j : j + M] for x in range(i, i + M))
        patterns.add(subgrid)

print(len(patterns))
