A = list(map(int, input().split()))
A.sort(reverse=True)
print(int(str(A[0]) + str(A[1])) + A[2])
