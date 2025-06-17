N, M = map(int, input().split())
S = [input() for _ in range(N)]
target = [
    "###.?????",
    "###.?????",
    "###.?????",
    "....?????",
    "?????????",
    "?????....",
    "?????.###",
    "?????.###",
    "?????.###",
]
n, m = len(target), len(target[0])

for y in range(N - n + 1):
    for x in range(M - m + 1):
        ok = True
        for dy in range(n):
            for dx in range(m):
                ok &= S[y + dy][x + dx] == target[dy][dx] or target[dy][dx] == "?"
        if ok:
            print(y + 1, x + 1)
