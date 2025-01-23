H, W = map(int, input().split())
si, sj = map(int, input().split())
maze = [list(input().strip()) for _ in range(H)]
x = input()

now = (si - 1, sj - 1)
for i in x:
    match i:
        case "L":
            dx, dy = 0, -1
            nx, ny = now[0] + dx, now[1] + dy
            if 0 > ny or maze[nx][ny] == "#":
                continue
            now = (nx, ny)
        case "R":
            dx, dy = 0, 1
            nx, ny = now[0] + dx, now[1] + dy
            if ny >= W or maze[nx][ny] == "#":
                continue
            now = (nx, ny)
        case "U":
            dx, dy = -1, 0
            nx, ny = now[0] + dx, now[1] + dy
            if 0 > nx or maze[nx][ny] == "#":
                continue
            now = (nx, ny)
        case "D":
            dx, dy = 1, 0
            nx, ny = now[0] + dx, now[1] + dy
            if nx >= H or maze[nx][ny] == "#":
                continue
            now = (nx, ny)

print(now[0] + 1, now[1] + 1)
