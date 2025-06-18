from itertools import permutations

from sortedcontainers import SortedSet

S, K = input().split()
K = int(K)

# 重複のある順列をsetで取り除き、SortedSetで辞書順に保持
perm_set = SortedSet("".join(p) for p in permutations(S))

# K番目 (1-indexed) の順列を取得
print(perm_set[K - 1])
