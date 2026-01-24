N = int(input())

flag = False
size = 0

for _ in range(N):
    A = int(input())

    if A == 1:
        size += 1

    elif A == 2:
        size = max(size - 1, 0)

    elif A == 3:
        flag = not flag

    if size >= 3 and flag:
        print("Yes")
    else:
        print("No")
