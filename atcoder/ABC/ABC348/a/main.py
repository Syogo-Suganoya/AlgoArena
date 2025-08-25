N = int(input())

for i in range(N):
    if (i + 1) % 3 == 0:
        print("x", end="")
    else:
        print("o", end="")
