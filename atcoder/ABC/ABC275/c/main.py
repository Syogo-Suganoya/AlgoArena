A = [list(input()) for _ in range(9)]
res = 0

# 正方形の左上を基準点とする
for i in range(9):
    for j in range(9):
        if A[i][j] != "#":
            continue

        # 正方形の右上の黒マスを探索
        for i2 in range(i, 9):
            for j2 in range(j + 1, 9):
                # 白マスならスキップ
                if A[i2][j2] != "#":
                    continue

                dx = i2 - i
                dy = j2 - j

                i3 = i2 + dy
                j3 = j2 - dx

                i4 = i + dy
                j4 = j - dx

                if 0 <= i3 < 9 and 0 <= j3 < 9 and 0 <= i4 < 9 and 0 <= j4 < 9:
                    if A[i3][j3] == "#" and A[i4][j4] == "#":
                        res += 1

print(res)
