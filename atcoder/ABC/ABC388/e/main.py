def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    # K 個の鏡餅を同時に作れるか？
    def can_make(K):
        # 小さい方: A[0..K-1]
        # 大きい方: A[N-K..N-1]
        for i in range(K):
            if A[i] * 2 > A[N - K + i]:
                return False
        return True

    # 二分探索
    left, right = 0, N // 2
    while left < right:
        mid = (left + right + 1) // 2
        if can_make(mid):
            left = mid
        else:
            right = mid - 1

    print(left)


solve()
