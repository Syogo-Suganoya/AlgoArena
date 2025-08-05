H, W, K = map(int, input().split())
maze = [list(input()) for _ in range(H)]

count = 0

# 行を削除するビット全探索（2^H 通り）
for row_mask in range(1 << H):
    # 列を削除するビット全探索（2^W 通り）
    for col_mask in range(1 << W):
        black = 0  # 黒マスのカウント
        for i in range(H):
            if (row_mask >> i) & 1:  # この行は削除対象
                continue
            for j in range(W):
                if (col_mask >> j) & 1:  # この列は削除対象
                    continue
                if maze[i][j] == "#":
                    black += 1
        if black == K:
            count += 1

print(count)
