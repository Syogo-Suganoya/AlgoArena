from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

# 5要素の組み合わせを直接計算
for comb in combinations(A, 5):
    product = 1
    for x in comb:
        product = product * x % P
    if product == Q:
        ans += 1

print(ans)
