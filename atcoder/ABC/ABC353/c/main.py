MOD = 10**8
N = int(input())
A = sorted(map(int, input().split()))

# 全ペアの単純和
total = sum(A) * (N - 1)

# 10^8 以上になるペア数を数える
import bisect

over = 0
for i in range(N):
    idx = bisect.bisect_left(A, MOD - A[i], i + 1)  # 後ろだけ見る
    over += N - idx

# 最終結果
ans = total - over * MOD
print(ans)
