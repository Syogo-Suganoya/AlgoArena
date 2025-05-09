import bisect

N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
ans = -1

for a in A:
    # 許容範囲を超えた位置を取得
    idx = bisect.bisect_right(B, a + D)
    if idx > 0:
        # 限界一歩手前を取得
        b = B[idx - 1]
        if abs(a - b) <= D:
            ans = max(ans, a + b)

print(ans)
