from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
result = []

for a in A:
    count[a] += 1
    if count[a] == 2:
        result.append(a)

print(*result)
