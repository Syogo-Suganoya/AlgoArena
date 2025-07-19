import math

T = int(input())
for _ in range(T):
    N = int(input())
    limit = int(N ** (1 / 3)) + 2  # およその3乗根（余裕を持って +2）
    for p in range(2, limit):
        if N % p == 0:
            # p が小さい方の素数候補
            pq = N // p
            if pq % p == 0:
                # p^2 が割り切れる場合：q = pq // p
                q = pq // p
            else:
                # p は q 側、q = pq
                q = p
                p = int(math.isqrt(pq))
            print(p, q)
            break
