from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# 各値の出現回数をカウント
c = Counter(A)

res = 0
# 各要素aについて、a-1, a, a+1の合計を調べて最大を更新
for a in c:
    total = c[a - 1] + c[a] + c[a + 1]
    res = max(res, total)

print(res)
