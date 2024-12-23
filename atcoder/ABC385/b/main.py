H, W, X, Y = map(int, input().split())
maze = [list(input()) for _ in range(H)]
T = list(input())

c = set()
x = X
y = Y

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


for i in T:
    match i:
        case "U":
            dx, dy = directions[0]
        case "D":
            dx, dy = directions[1]
        case "L":
            dx, dy = directions[2]
        case "R":
            dx, dy = directions[3]
    tmp_x = x + dx
    tmp_y = y + dy
    if (
        tmp_x < 0
        or tmp_x >= H
        or tmp_y < 0
        or tmp_y >= W
        or maze[tmp_x - 1][tmp_y - 1] == "#"
    ):
        continue
    x = tmp_x
    y = tmp_y
    if maze[x - 1][y - 1] == "@":
        c.add((x - 1, y - 1))


print(x, y, len(c))
