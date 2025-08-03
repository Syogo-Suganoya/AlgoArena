H, W, X, Y = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# 0-indexed に変換
X -= 1
Y -= 1

# 最初に起点をカウント
res = 1

# 上方向
i = X - 1
while i >= 0 and maze[i][Y] == ".":
    res += 1
    i -= 1

# 下方向
i = X + 1
while i < H and maze[i][Y] == ".":
    res += 1
    i += 1

# 左方向
j = Y - 1
while j >= 0 and maze[X][j] == ".":
    res += 1
    j -= 1

# 右方向
j = Y + 1
while j < W and maze[X][j] == ".":
    res += 1
    j += 1

print(res)

"""
H, W, X, Y = map(int, input().split())
maze = [list(input()) for _ in range(H)]
X,Yを起点
上下4方向をループ
そこから直線に進めるだけ直進
壁がぶつかるまで
進めた距離を出力
"""
