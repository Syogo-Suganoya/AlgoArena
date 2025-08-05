N, K = map(int, input().split())
A = list(map(int, input().split()))

path = []
seen = set()
cur = 0

# ループが始まるまでたどる
while cur not in seen:
    seen.add(cur)
    path.append(cur)
    cur = A[cur] - 1

# ループの始まりのインデックスを path から探す
loop_start = path.index(cur)
loop_len = len(path) - loop_start

if K < loop_start:
    print(path[K] + 1)
else:
    idx = loop_start + (K - loop_start) % loop_len
    print(path[idx] + 1)
