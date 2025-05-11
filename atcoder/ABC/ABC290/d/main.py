import math

# 複数のテストケースに対応
T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())
    # NとDの最大公約数を求める
    # g 個の独立な巡回クラスが存在することになる（mod Nの世界で）
    g = math.gcd(N, D)

    # 1つの巡回クラスの長さ（= 印がつく間隔の周期）
    cycle_length = N // g

    # K番目の印がどの巡回クラスに属するかを求める（0始まりにしているので K-1）
    q = (K - 1) // cycle_length

    # その巡回クラスの中で何番目か
    r = (K - 1) % cycle_length

    # 実際の位置を求める。D*rで進み、q個分巡回クラスの分だけずれる
    print((D * r + q) % N)
