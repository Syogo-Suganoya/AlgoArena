N = int(input())
A = list(map(int, input().split()))

res = 0

for l in range(N):
    for r in range(l + 1, N + 1):
        s = sum(A[l:r])

        for j in range(l, r):
            if s % A[j] == 0:
                break
        else:
            res += 1

print(res)
