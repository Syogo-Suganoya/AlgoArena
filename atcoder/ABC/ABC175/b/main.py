from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

ans = 0
for a, b, c in combinations(L, 3):
    # 1. 長さがすべて異なるか
    if len({a, b, c}) < 3:
        continue
    # 2. 三角形の成立条件
    if a + b + c > 2 * max(a, b, c):
        ans += 1

print(ans)
