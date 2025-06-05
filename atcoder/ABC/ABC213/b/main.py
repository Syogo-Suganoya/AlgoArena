N = int(input())
A = list(map(int, input().split()))
sa = sorted(A)
print(A.index(sa[-2]) + 1)
