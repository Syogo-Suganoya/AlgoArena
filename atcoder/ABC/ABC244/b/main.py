N = int(input())
S = input()

x, y = 0, 0
ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dir = 0

for c in S:
    if c == "S":
        dx, dy = ds[dir]
        x += dx
        y += dy
    elif c == "R":
        dir = (dir + 1) % 4  # 右回転

print(x, y)
