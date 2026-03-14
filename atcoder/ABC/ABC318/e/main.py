N = int(input())
A = list(map(int, input().split()))

MAX = max(A) + 1

left = [0] * MAX
right = [0] * MAX

for a in A:
    right[a] += 1

tmp = 0
ans = 0

for i in range(N):
    a = A[i]

    tmp -= left[a] * right[a]

    right[a] -= 1

    ans += tmp

    left[a] += 1

    tmp += left[a] * right[a]

print(ans)
