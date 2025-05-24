N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
for i in range(N):
    t = A[i] * 10 / 3 / 10 + B[i] * 10 / 3 * 2 / 10
    res += t
print(res)
