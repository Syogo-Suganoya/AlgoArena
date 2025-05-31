N = int(input())
A = list(map(int, input().split()))

res = []
for i in range(N):
    week_sum = sum(A[i * 7 : i * 7 + 7])
    res.append(week_sum)

print(*res)
