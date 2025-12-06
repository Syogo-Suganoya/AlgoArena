N = int(input())
A = list(map(int, input().split()))

right = A[0]
ans = 1

for cur in range(1, N):
    if cur >= right:
        break
    ans += 1
    right = max(cur + A[cur], right)

print(ans)
