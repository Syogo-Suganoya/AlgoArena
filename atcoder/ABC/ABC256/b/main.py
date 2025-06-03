N = int(input())
A = list(map(int, input().split()))

total = sum(A)

count = 0
for i in range(N):
    if total >= 4:
        count += 1
    total -= A[i]

print(count)
