from sortedcontainers import SortedList

N, M, K = map(int, input().split())
A = SortedList(map(int, input().split()))
B = SortedList(map(int, input().split()))

count = 0
for a in A:
    idx = B.bisect_left(a)
    if idx == len(B):
        continue
    B.pop(idx)
    count += 1
print("Yes" if count >= K else "No")
