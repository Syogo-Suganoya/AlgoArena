import sys

sys.setrecursionlimit(10**7)

N, H, W = map(int, input().split())
tiles = [tuple(map(int, input().split())) for _ in range(N)]

board = [[0] * W for _ in range(H)]
used = [False] * N


def find_first_empty():
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def can_place(i, j, h, w):
    if i + h > H or j + w > W:
        return False
    for x in range(i, i + h):
        for y in range(j, j + w):
            if board[x][y] == 1:
                return False
    return True


def place(i, j, h, w, val):
    for x in range(i, i + h):
        for y in range(j, j + w):
            board[x][y] = val


def dfs():
    i, j = find_first_empty()
    if i == -1:
        return True

    for k in range(N):
        if used[k]:
            continue
        for h, w in [(tiles[k][0], tiles[k][1]), (tiles[k][1], tiles[k][0])]:
            if can_place(i, j, h, w):
                place(i, j, h, w, 1)
                used[k] = True
                if dfs():
                    return True
                used[k] = False
                place(i, j, h, w, 0)
    return False


print("Yes" if dfs() else "No")
