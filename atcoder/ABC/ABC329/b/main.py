from sortedcontainers import SortedSet

N = int(input())
A = list(map(int, input().split()))

A = SortedSet(A)

print(A[-2])
