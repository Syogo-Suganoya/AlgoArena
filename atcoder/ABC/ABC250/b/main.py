N, A, B = map(int, input().split())

wb = [["."] * B for _ in range(A)]
bb = [["#"] * B for _ in range(A)]

alb = [wb, bb]

# ブロック単位で交互に描画
for i in range(N):
    for ai in range(A):  # 各ブロックの高さ分ループ
        f = i % 2  # 横方向の最初の色を切り替えるフラグ
        row = []
        for j in range(N):
            row.extend(alb[f][ai])  # 横方向にブロックを並べる
            f ^= 1  # 色を交互に切り替え
        print("".join(row))  # 1行をまとめて出力
