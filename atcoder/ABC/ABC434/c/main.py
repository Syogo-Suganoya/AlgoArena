T = int(input())

for _ in range(T):
    N, H = map(int, input().split())

    low = high = H
    pre_t = 0
    ok = True

    for _ in range(N):
        t, l, u = map(int, input().split())

        times = t - pre_t

        low -= times
        high += times
        # 範囲
        low = max(low, l)
        high = min(high, u)
        # 矛盾
        if low > high:
            ok = False

        pre_t = t

    print("Yes" if ok else "No")
