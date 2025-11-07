from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 1. 各 i について i + A[i] の出現回数を集計
count = defaultdict(int)
for i in range(N):
    key = i + A[i]
    count[key] += 1

# 2. 各 i について j - i == A[i] + A[j] となるペアを数える
ans = 0
for i in range(N):
    key = i - A[i]
    ans += count[key]

print(ans)
