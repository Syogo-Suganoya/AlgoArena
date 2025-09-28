H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

# 上下左右の方向ベクトル
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# グリッド内かどうか判定
def in_grid(x, y):
    return 0 <= x < H and 0 <= y < W


# (x, y) の周囲にある黒マス（"#"）の数を数える
def count(x, y):
    c = 0
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if in_grid(nx, ny) and S[nx][ny] == "#":
            c += 1
    return c


# 反復的に白マスを黒マスに変える処理
for i in range(H * W):  # 最大でも H*W 回繰り返せば収束する
    if i == 0:
        # 初期ステップ: 周囲に黒マスが1つだけある白マスをリストに入れる
        T = []
        for x in range(H):
            for y in range(W):
                if S[x][y] == "." and count(x, y) == 1:
                    T.append((x, y))
    else:
        # 次のステップ: 前回変換したマスの隣接セルを調べて、
        # 周囲に黒マスが1つだけある白マスを集める
        nT = []
        for x, y in T:
            for dx, dy in dxdy:
                nx, ny = x + dx, y + dy
                if in_grid(nx, ny) and S[nx][ny] == "." and count(nx, ny) == 1:
                    nT.append((nx, ny))
        T = nT

    # これ以上変換できるマスがないなら終了
    if len(T) == 0:
        break

    # 条件を満たした白マスを黒マスに変換する
    for x, y in T:
        S[x][y] = "#"


# 最終的な黒マスの個数を数える
ans = 0
for x in range(H):
    for y in range(W):
        ans += int(S[x][y] == "#")

print(ans)
