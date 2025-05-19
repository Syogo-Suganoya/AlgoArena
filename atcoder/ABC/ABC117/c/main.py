N, M = map(int, input().split())
X = list(map(int, input().split()))


def main():
    # 特殊ケース：コマの数が地点の数以上なら移動は不要
    if N >= M:
        return 0

    X.sort()
    # 隣接する地点間の距離を計算
    distances = [X[i + 1] - X[i] for i in range(M - 1)]

    # 距離を昇順にソート
    distances.sort()

    # 最小の移動距離は、距離の小さい M−N 個の区間の合計
    return sum(distances[: M - N])
