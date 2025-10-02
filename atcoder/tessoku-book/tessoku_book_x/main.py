import bisect


def lis(A):
    L = []  # LISの末尾候補を管理する配列
    for x in A:
        idx = bisect.bisect_left(L, x)  # L内でxを挿入できる位置
        if idx == len(L):
            L.append(x)  # xが一番大きい → LISを伸ばせる
        else:
            L[idx] = x  # より小さい値で末尾を更新
    return len(L)


N = int(input())
A = list(map(int, input().split()))

print(lis(A))
