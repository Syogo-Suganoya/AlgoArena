N = int(input())
maze1 = [list(input()) for _ in range(N)]
maze2 = [list(input()) for _ in range(N)]


def rotate(maze):
    """90°時計回りに回転"""
    return [[maze[N - 1 - j][i] for j in range(N)] for i in range(N)]


ans = N * N  # 最大値で初期化

# 0°, 90°, 180°, 270° の4回ループ
for r in range(4):
    # maze1 と maze2 の異なるマスの数をカウント
    diff = sum(maze1[i][j] != maze2[i][j] for i in range(N) for j in range(N)) + r
    ans = min(ans, diff)
    # 90°回転
    maze1 = rotate(maze1)

print(ans)
