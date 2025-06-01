import bisect

N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

for a in reversed(A):
    # B から a に一番近い位置を二分探索
    idx = bisect.bisect_right(B, a + D)
    if idx > 0:
        # 差が D 以下なら、和の最大値を更新
        b = B[idx - 1]
        if abs(a - b) <= D:
            print(a + b)
            exit()

print(-1)
