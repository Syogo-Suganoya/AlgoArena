import math

T = int(input())

for _ in range(T):
    N = int(input())

    # N = p^2 * q か N = p * q^2 という形で分解できるか調べる
    for x in range(2, int(1e6) + 1):
        # まず、x^2 が N を割り切れる場合を調べる
        if N % (x * x) == 0:
            p = x
            q = N // (x * x)
            # 形: N = p^2 * q
            print(p, q)
            break
        # それがダメなら、x が N を割り切れる場合を調べる
        elif N % x == 0:
            q = x
            p_sq = N // x
            # ここで、p^2 = N / q であることを確認
            p = int(math.isqrt(p_sq))
            if p * p == p_sq:
                # 形: N = q * p^2
                print(p, q)
                break
