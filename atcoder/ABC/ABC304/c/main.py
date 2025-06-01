N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

infected = [False] * N
infected[0] = True

# 感染者のリストをスタックとして管理
stack = [0]

while stack:
    i = stack.pop()
    xi, yi = XY[i]
    for j in range(N):
        if infected[j]:
            continue
        xj, yj = XY[j]
        dx = xi - xj
        dy = yi - yj
        if dx * dx + dy * dy <= D * D:
            infected[j] = True
            stack.append(j)

for i in range(N):
    print("Yes" if infected[i] else "No")
