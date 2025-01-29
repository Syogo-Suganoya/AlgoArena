N = int(input())

A = 1
while A**A <= N:
    if A**A == N:
        print(A)
        break
    A += 1
else:
    print(-1)
