from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
result = 0

for i, a in enumerate(A, start=1):
    result += cnt[i - a]
    cnt[i + a] += 1

print(result)
