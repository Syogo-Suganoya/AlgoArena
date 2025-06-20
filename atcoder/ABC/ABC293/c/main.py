from itertools import product

H, W = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(H)]

res = 0
steps = H + W - 2

for bits in product([0, 1], repeat=steps):  # 0:右, 1:下
    if bits.count(1) != H - 1:
        continue  # 下に行く回数が合わないとゴールできない

    y, x = 0, 0
    s = set()
    s.add(maze[y][x])

    for b in bits:
        if b == 0:
            x += 1
        else:
            y += 1
        val = maze[y][x]
        if val in s:
            break
        s.add(val)

    if len(s) == H + W - 1:
        res += 1

print(res)
