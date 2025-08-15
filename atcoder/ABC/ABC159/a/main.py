N, M = map(int, input().split())  # N: 偶数の個数, M: 奇数の個数


def C2(x):  # xC2 = x*(x-1)/2
    return x * (x - 1) // 2


even_pairs = C2(N) + C2(M)
print(even_pairs)
