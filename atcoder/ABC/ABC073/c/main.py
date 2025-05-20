from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

c = Counter(A)

res = 0
# 出現回数が奇数のものをカウント
for i in c.values():
    if i % 2 == 1:
        res += 1

print(res)
