N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import Counter

# B の出現回数をカウント
countB = Counter(B)

result = []
for a in A:
    # まだ削除すべき B が残っているならスキップ
    if countB[a] > 0:
        countB[a] -= 1
    else:
        result.append(a)

print(*result)
