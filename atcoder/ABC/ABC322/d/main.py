import copy
import sys

sys.setrecursionlimit(10000)


# 右に 90 度回転
def rotate(piece):
    return [[piece[3 - j][i] for j in range(4)] for i in range(4)]


# グリッド内判定
def in_grid(i, j):
    return 0 <= i < 4 and 0 <= j < 4


# 基準位置 (di,dj) に配置できるかチェックし、配置した状態を返す
def can_put(exist, piece, di, dj):
    new_exist = copy.deepcopy(exist)
    for i in range(4):
        for j in range(4):
            if piece[i][j] == "#":
                ni, nj = i + di, j + dj
                if not in_grid(ni, nj):
                    return None
                if new_exist[ni][nj] == 1:
                    return None
                new_exist[ni][nj] = 1
    return new_exist


# 再帰でポリオミノを置く
def dfs(idx, exist, pieces):
    if idx == 3:
        if all(all(row) for row in exist):
            print("Yes")
            sys.exit(0)
        return
    for di in range(-3, 4):
        for dj in range(-3, 4):
            new_exist = can_put(exist, pieces[idx], di, dj)
            if new_exist is not None:
                dfs(idx + 1, new_exist, pieces)


# 入力
pieces = []
for _ in range(3):
    piece = [list(input()) for _ in range(4)]
    pieces.append(piece)

# 4回回転させながら全探索
for _ in range(4):
    for _ in range(4):
        dfs(0, [[0] * 4 for _ in range(4)], pieces)
        pieces[2] = rotate(pieces[2])
    pieces[1] = rotate(pieces[1])

print("No")
