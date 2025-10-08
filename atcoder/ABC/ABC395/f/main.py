def can_achieve(H, N, X, U, D):
    # 上の歯の長さが取り得る範囲を計算
    min_u = max(0, H - D[0])
    max_u = min(U[0], H)
    for i in range(1, N):
        min_u = max(min_u - X, H - D[i])
        max_u = min(max_u + X, U[i])
        if min_u > max_u:
            return False
    return True


def min_cost(N, X, U, D):
    # 二分探索で最大のHを求める
    left, right = 0, min(U[i] + D[i] for i in range(N)) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if can_achieve(mid, N, X, U, D):
            left = mid
        else:
            right = mid
    H = left
    # 最小費用の計算
    total_cost = sum(U[i] + D[i] for i in range(N)) - N * H
    return total_cost


# 入力の読み込み
N, X = map(int, input().split())
U = []
D = []
for _ in range(N):
    u, d = map(int, input().split())
    U.append(u)
    D.append(d)

# 最小費用の計算と出力
print(min_cost(N, X, U, D))
