from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
ans = 0

for v in cnt.values():
    if v < 2:
        continue
    comb2 = v * (v - 1) // 2
    rem = N - v
    ans += comb2 * rem

print(ans)
