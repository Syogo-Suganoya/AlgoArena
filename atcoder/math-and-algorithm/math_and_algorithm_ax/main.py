N, X, Y = map(int, input().split())
D = abs(X) + abs(Y)

if N >= D and (N - D) % 2 == 0:
    print("Yes")
else:
    print("No")
