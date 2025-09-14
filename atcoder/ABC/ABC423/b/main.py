N = int(input())
A = list(map(int, input().split()))

if A.count(1) <= 1:
    print(0)
else:
    l = A.index(1)
    r = N - 1 - A[::-1].index(1)
    print(r - l)
