N = int(input())
T = input()

now = (0, 0)
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
now_dir = 0
for i in T:
    match i:
        case "S":
            now = (now[0] + dir[now_dir][0], now[1] + dir[now_dir][1])
        case "R":
            now_dir += 1
            now_dir %= 4

print(*now)
