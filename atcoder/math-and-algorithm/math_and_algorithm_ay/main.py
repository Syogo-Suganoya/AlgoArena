N = int(input())
seen = [2, 4, 8, 6]
print(seen[(N - 1) % len(seen)])
