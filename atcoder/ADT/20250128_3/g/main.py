from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

s = SortedList(P[: K - 1])

for i in range(K - 1, N):
    s.add(P[i])
    print(s[-K])
