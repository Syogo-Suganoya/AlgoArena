def min_inconvenience(N, coordinates):
    # x座標とy座標をそれぞれ取り出す
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]

    # x座標とy座標をソート
    x_coords.sort()
    y_coords.sort()

    # 中央値を計算
    median_x = x_coords[N // 2]
    median_y = y_coords[N // 2]

    # 不便さを計算
    inconvenience = sum(abs(x - median_x) + abs(y - median_y) for x, y in coordinates)
    return inconvenience


# 入力の処理
N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

# 結果の出力
print(min_inconvenience(N, coordinates))
