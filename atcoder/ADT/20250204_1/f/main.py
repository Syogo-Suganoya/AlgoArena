from itertools import combinations

n, m = list(map(int, input().split()))
# 狭義単調増加
for l in combinations(range(1, m + 1), n):
    print(*l, sep=" ")
