W, H, x, y = map(int, input().split())

# 面積の半分 (小さい領域を最大化するなら半分が答え)
area_half = W * H / 2

# 点が中心かチェック
if 2 * x == W and 2 * y == H:
    # 中心にある → 切り方はいろいろある
    print(area_half, 1)
else:
    # 中心でない → 切り方は 1 通りだけ
    print(area_half, 0)
