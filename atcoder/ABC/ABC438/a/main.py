N, M = map(int, input().split())

ans = (M - N % 7 - 1) % 7 + 1
print(ans)
