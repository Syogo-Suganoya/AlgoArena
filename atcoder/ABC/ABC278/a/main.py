N, K = map(int, input().split())
A = list(map(int, input().split()))

res = A[K:] + [0] * min(N, K)
print(*res)
