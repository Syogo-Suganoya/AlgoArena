N, K = map(int, input().split())
A = list(map(int, input().split()))


# ある長さ L 以下にすべての丸太を収められるか判定する関数
def can(L):
    cuts = 0
    for x in A:
        # x を L 以下の長さにするには、
        # ceil(x / L) - 1 回の切断が必要
        # → (x - 1) // L がそれと同じ意味
        cuts += (x - 1) // L
        if cuts > K:  # K を越えた時点で不可能
            return False
    return True  # 制限内に収まるならOK


# 二分探索：最小 L を探す
left, right = 1, max(A)

while left < right:
    mid = (left + right) // 2
    if can(mid):
        right = mid  # mid で可能 → もっと小さくしてよい
    else:
        left = mid + 1  # mid では不可能 → もっと大きい必要がある

print(left)
