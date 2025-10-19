from collections import defaultdict

N, M = map(int, input().split())
S = input().strip()

count = defaultdict(int)

for i in range(N - M + 1):
    sub = S[i : i + M]
    count[sub] += 1

max_count = max(count.values())
max_subs = [k for k, v in count.items() if v == max_count]

max_subs.sort()
print(max_count)
print(*max_subs)
