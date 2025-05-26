N = int(input())
A = list(map(int, input().split()))
sa = sorted(A, reverse=True)
print(A.index(sa[1]) + 1)
