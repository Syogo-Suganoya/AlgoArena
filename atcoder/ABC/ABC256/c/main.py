h1, h2, h3, w1, w2, w3 = map(int, input().split())

count = 0

for a in range(1, 31):
    for b in range(1, 31):
        for c in range(1, 31):
            for d in range(1, 31):
                e = h1 - a - b  # [0,2]
                f = h2 - c - d  # [1,2]
                if e <= 0 or f <= 0:
                    continue

                g = w1 - a - c
                h = w2 - b - d
                if g <= 0 or h <= 0:
                    continue

                i = h3 - g - h
                if i <= 0:
                    continue

                if e + f + i != w3:
                    continue

                # 条件をすべて満たすのでカウント
                count += 1

print(count)
