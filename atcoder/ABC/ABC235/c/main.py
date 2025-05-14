from collections import defaultdict

N, Q = map(int, input().split())
S = list(map(int, input().split()))

# l[x] = xが出現するインデックスのリスト
l = defaultdict(list)

for idx, val in enumerate(S):
    l[val].append(idx + 1)  # 1-indexedで格納

for _ in range(Q):
    x, k = map(int, input().split())
    if len(l[x]) < k:
        print(-1)
    else:
        print(l[x][k - 1])
