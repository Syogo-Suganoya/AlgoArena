def monochromatic_subgrid():
    max_area = 0

    # 行の選択を全探索（ビット全探索）
    for row_mask in range(1, 1 << H):
        count = {}
        # 選択した行での列の値を確認
        for col in range(W):
            val = None
            valid = True
            for row in range(H):
                if not (row_mask & (1 << row)):  # 選択された行
                    continue
                if val is None:
                    val = P[row][col]
                elif val != P[row][col]:
                    valid = False
                    break
            if valid:
                count[val] = count.get(val, 0) + 1

        # 最大の列数を取得し、部分グリッドの面積を計算
        if count:
            max_cols = max(count.values())
            max_area = max(max_area, max_cols * bin(row_mask).count("1"))

    return max_area


# 入力例
H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

# 出力
print(monochromatic_subgrid())
