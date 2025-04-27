N = int(input())

# 最初は全て白（'.'）の NxN 二次元配列を作成
grid = [["." for _ in range(N)] for _ in range(N)]

for i in range(0, (N // 2) + 1, 2):
    for j in range(i, N - i):
        # 右に移動する分
        # (i,i)からN-iマス数分
        grid[i][j] = "#"
        # (N-i,i)からN-iマス数分右
        grid[N - i - 1][j] = "#"

        # 下に移動分
        # (i,i)からN-iマス数分
        grid[j][i] = "#"
        # (N-i,i)からN-iマス数分下に移動
        grid[j][N - i - 1] = "#"

# 出力
for row in grid:
    print("".join(row))
