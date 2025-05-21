H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

# グリッド初期化
grid = [[0] * W for _ in range(H)]

color = 1  # 現在使用中の色（1番から）
index = 0  # 現在の色のAのインデックス
remain = A[0]  # 現在の色で塗る残りのマス数

# グリッドをジグザグに走査して塗る
for i in range(H):
    # 偶数行: 左→右、奇数行: 右→左
    cols = range(W) if i % 2 == 0 else reversed(range(W))
    for j in cols:
        grid[i][j] = color  # 現在のマスを現在の色で塗る
        remain -= 1  # 残りの塗りマスを1つ減らす

        if remain == 0 and index + 1 < N:
            index += 1  # 次の色へ
            color = index + 1
            remain = A[index]  # 次の色の塗るマス数をセット

# 出力
for row in grid:
    print(" ".join(map(str, row)))
