# 入力の読み込み
H, W = map(int, input().split())  # グリッドの高さと幅
grid = [input().strip() for _ in range(H)]  # グリッド情報

top, left, bottom, right = H, W, -1, -1

# 最も上下左右の位置を探す
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            top = min(top, i)
            left = min(left, j)
            bottom = max(bottom, i)
            right = max(right, j)

# 指定範囲内に "." が含まれているかチェック
is_valid = True
for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if grid[i][j] == ".":
            is_valid = False
            break

# 結果を出力
print("Yes" if is_valid else "No")
