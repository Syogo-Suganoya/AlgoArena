import math

N, M = map(int, input().split())
ans = float("inf")

# a を 1 から √M まで試す（a > √M の場合、b < √M なので a*b は単調増加になり効率が良い）
for a in range(1, min(N, int(math.isqrt(M)) + 1) + 1):
    # b は M を a で割ったときの切り上げ (ceil)
    b = (M + a - 1) // a  # ceil(M / a)

    # b が N 以下であれば a*b は有効な候補
    if b <= N:
        ans = min(ans, a * b)  # 条件を満たす中で最小の a*b を更新

print(ans if ans != float("inf") else -1)
