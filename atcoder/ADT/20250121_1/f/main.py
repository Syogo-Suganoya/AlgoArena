def is_valid_sudoku(grid):
    # 行と列の検証
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            # 行の検証
            if grid[i][j] in row:
                return False
            row.add(grid[i][j])
            # 列の検証
            if grid[j][i] in col:
                return False
            col.add(grid[j][i])

    # 3x3 ブロックの検証
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set()
            for k in range(3):
                for l in range(3):
                    num = grid[i + k][j + l]
                    if num in block:
                        return False
                    block.add(num)

    return True


# 入力の読み込み
grid = []
for _ in range(9):
    grid.append(list(map(int, input().split())))

# 結果の出力
if is_valid_sudoku(grid):
    print("Yes")
else:
    print("No")
