N = int(input())
grid = [input() for _ in range(N)]

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

max_number = "0"

for i in range(N):
    for j in range(N):
        for dx, dy in directions:
            x, y = i, j
            number = ""
            for _ in range(N):
                number += grid[x][y]
                x = (x + dx) % N
                y = (y + dy) % N
            if number > max_number:
                max_number = number

print(max_number)
