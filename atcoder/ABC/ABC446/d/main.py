from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

pos = {}
for i, x in enumerate(A):
    if x not in pos:
        pos[x] = []
    pos[x].append(i)

visited = set()
max_len = 0

for i in range(N):
    if i in visited:
        continue
    length = 1
    current = A[i]
    visited.add(i)
    idx = i

    while True:
        next_val = current + 1
        if next_val not in pos:
            break
        indices = pos[next_val]
        j = bisect_left(indices, idx + 1)
        if j == len(indices):
            break
        idx = indices[j]
        visited.add(idx)
        current = next_val
        length += 1

    max_len = max(max_len, length)

print(max_len)
