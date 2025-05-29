N = int(input())
maze = [list(input()) for _ in range(N)]

row_o_count = [0] * N
col_o_count = [0] * N

# 各行の'o'数カウント
for i in range(N):
    row_o_count[i] = maze[i].count("o")

# 各列の'o'数カウント
for j in range(N):
    col_o_count[j] = sum(maze[i][j] == "o" for i in range(N))

res = 0
for i in range(N):
    for j in range(N):
        if maze[i][j] == "o":
            res += (row_o_count[i] - 1) * (col_o_count[j] - 1)

print(res)
