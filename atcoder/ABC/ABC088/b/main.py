N = int(input())
A = list(map(int, input().split()))

resultA = 0
resultB = 0
A.sort(reverse=True)

to = "A"
for i in range(N):
    if to == "A":
        resultA += A[i]
        to = "B"
        continue
    resultB += A[i]
    to = "A"

print(resultA - resultB)
