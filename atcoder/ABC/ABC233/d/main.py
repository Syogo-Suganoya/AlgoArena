from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = defaultdict(int)
count[0] = 1  # 初期値として累積和0が1回出現

ans = 0
cum_sum = 0

for a in A:
    cum_sum += a
    ans += count[cum_sum - K]
    count[cum_sum] += 1

print(ans)
