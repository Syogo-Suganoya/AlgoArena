N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * N
for i in range(N):
    if A[i] <= L:
        ans[i] = L
    elif A[i] >= R:
        ans[i] = R
    else:
        ans[i] = A[i]

print(*ans)
