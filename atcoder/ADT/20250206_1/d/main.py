from sortedcontainers import SortedSet

N = int(input())
A = list(map(int, input().split()))

a = SortedSet(A)
print(a[-2])
