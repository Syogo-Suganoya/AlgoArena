N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for c in B:
    res += A[c - 1]
print(res)
