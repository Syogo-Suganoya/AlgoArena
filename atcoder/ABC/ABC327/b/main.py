N = int(input())

A = 1
while True:
    power = A**A
    if power == N:
        print(A)
        break
    elif power > N:
        print(-1)
        break
    A += 1
