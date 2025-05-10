H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W - 1):  # j+1を見るのでW-1まで
        if maze[i][j] == "T" and maze[i][j + 1] == "T":
            maze[i][j] = "P"
            maze[i][j + 1] = "C"

for row in maze:
    print("".join(row))
