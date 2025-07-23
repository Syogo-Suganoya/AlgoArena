N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    t = A[i - 1]
    t = min(N, t + 1)
    if t not in A:
        A[i - 1] = t
print(*A)
