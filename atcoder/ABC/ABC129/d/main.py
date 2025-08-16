# 入力
H, W = map(int, input().split())
fi = [input().strip() for _ in range(H)]

# 前処理用の配列
Left = [[0] * W for _ in range(H)]
Right = [[0] * W for _ in range(H)]
Up = [[0] * W for _ in range(H)]
Down = [[0] * W for _ in range(H)]

# 左方向の連続空マス
for i in range(H):
    cur = 0
    for j in range(W):
        if fi[i][j] == "#":
            cur = 0
        else:
            cur += 1
        Left[i][j] = cur

# 右方向の連続空マス
for i in range(H):
    cur = 0
    for j in reversed(range(W)):
        if fi[i][j] == "#":
            cur = 0
        else:
            cur += 1
        Right[i][j] = cur

# 上方向の連続空マス
for j in range(W):
    cur = 0
    for i in range(H):
        if fi[i][j] == "#":
            cur = 0
        else:
            cur += 1
        Up[i][j] = cur

# 下方向の連続空マス
for j in range(W):
    cur = 0
    for i in reversed(range(H)):
        if fi[i][j] == "#":
            cur = 0
        else:
            cur += 1
        Down[i][j] = cur

# 集計
res = 0
for i in range(H):
    for j in range(W):
        if fi[i][j] == "#":
            continue
        # 交差マスを重複カウントしているので3引く
        res = max(res, Left[i][j] + Right[i][j] + Up[i][j] + Down[i][j] - 3)

print(res)
