from itertools import product


def max_humidified_area(h, w, d, s):
    ans = 0
    # 床のマスを探索
    for i1, j1 in product(range(h), range(w)):
        if s[i1][j1] == "#":
            continue  # 床のマスではない
        for i2, j2 in product(range(h), range(w)):
            if s[i2][j2] == "#" or (i1 == i2 and j1 == j2):
                continue  # 床のマスではないか、同じ位置
            tmp = 0
            for i, j in product(range(h), range(w)):
                if s[i][j] == "." and (
                    abs(i - i1) + abs(j - j1) <= d or abs(i - i2) + abs(j - j2) <= d
                ):
                    tmp += 1  # 加湿されている
            ans = max(ans, tmp)
    return ans


# 入力
H, W, D = map(int, input().split())
S = [input() for _ in range(H)]
# 計算
result = max_humidified_area(H, W, D, S)
# 出力
print(result)
