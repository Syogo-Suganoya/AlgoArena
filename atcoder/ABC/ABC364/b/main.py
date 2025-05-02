H, W = map(int, input().split())
Si, Sj = map(int, input().split())
maze = [list(input()) for _ in range(H)]
X = list(input())

now = (Si - 1, Sj - 1)

for c in X:
    match c:
        case "L":
            d = (0, -1)
        case "R":
            d = (0, 1)
        case "U":
            d = (-1, 0)
        case "D":
            d = (1, 0)

    nx = now[0] + d[0]
    ny = now[1] + d[1]
    if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == ".":
        now = (nx, ny)

print(now[0] + 1, now[1] + 1)
