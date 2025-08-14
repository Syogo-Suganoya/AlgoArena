N = int(input())
ans = 0
for A in range(1, N):
    # Bの取りうる上限
    maxB = (N - 1) // A
    ans += maxB
print(ans)
