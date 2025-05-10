maze = [list(input()) for _ in range(8)]

for i in range(8):
    for j in range(8):
        if maze[i][j] == "*":
            a = 9 - i - 1
            b = j
            print(chr(b + ord("a")) + str(a))
